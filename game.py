import re 
import random
import sys
import sqlite3
class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.username = None
        self.user_id = None
    def add_question(self, questions):
        self.questions.extend(questions)

    def take_username(self):
        while True:
            try:
                user_input = input("\nEnter username (alphanumeric): ")

                if re.match(r"^\w+$", user_input):
                    print("Username accepted")
                    break
                else:
                    print("Username must be alphanumeric")
            except KeyboardInterrupt:
                print("\nExit")
                sys.exit()
        self.username = user_input
        try:
            conn = sqlite3.connect('quiz_data.db')
            cursor = conn.cursor()

            cursor.execute("SELECT user_id FROM USERS WHERE username=?",(self.username,))
            result = cursor.fetchone()

            if result:
                self.user_id = result[0]
                print(f"Welcome back, {self.username}!")
            else:
                cursor.execute("INSERT INTO Users (username) VALUES (?)",(self.username,))
                self.user_id = cursor.lastrowid
                print(f"Welcome to the game, {self.username}")
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print(f"Database error while loading user: {error}")
    def start_game(self):
        if not self.username:
            print("Please set a username first.")
        random.shuffle(self.questions)
        for q in self.questions:
            q.display()
            while True:
                try:
                    answer = int(input("Select option (0 to exit): "))

                    if answer == 0:
                        return

                    if 1 <= answer <= len(q.options):
                        if answer == q.answer:
                            print("Correct!")
                            self.score += 1
                        else:
                            correct = q.options[q.answer - 1]
                            print(f"Wrong! Correct answer: {correct}")
                        break
                    else:
                        print(f"Please select a number between 1 and {len(q.options)}")

                except ValueError:
                    print("Please enter a valid number")

    def display_score(self):
        print(f"\n--- {self.username}'s Final Score: {self.score}/{len(self.questions)} ---")

        try:
            conn = sqlite3.connect('quiz_data.db')
            cursor = conn.cursor()

            cursor.execute("SELECT top_score From Scores WHERE user_id = ?",(self.user_id,))
            result = cursor.fetchone()

            if result:
                past_top_score = result[0]
                if self.score > past_top_score:
                    cursor.execute("UPDATE Scores SET top_score = ? WHERE user_id = ?",(self.score, self.user_id))
            else:
                cursor.execute("INSERT INTO Scores (user_id, top_score) VALUES (?, ?)", (self.user_id, self.score))
                
            print("\n🏆 Top 5 Highest Scorers 🏆")
            
            # Leaderboard   
            leaderboard_query = """
                SELECT Users.username, Scores.top_score 
                FROM Scores 
                JOIN Users ON Scores.user_id = Users.user_id 
                ORDER BY Scores.top_score DESC 
                LIMIT 5 
            """
            cursor.execute(leaderboard_query)
            top_scorers = cursor.fetchall()

            for i, row in enumerate(top_scorers, start=1):
                # row[0] is the username, row[1] is the top_score
                print(f"{i}. {row[0]} - {row[1]}")

            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print(f"Database error while handling scores: {error}")
