# QuizGame
#  ├── questions
#  ├── score
#  ├── username
#  └── start_game()

# Question
#  ├── text
#  ├── options
#  └── answer
import re
import sys
import json
import random
import os
class Question:
    def __init__(self, id, text, options, answer):
        self._id = id
        self.text = text
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n{self._id}. {self.text}\n")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")


class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.username = None

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
        file_path = "score.json"
        new_score_entry = {
            "username": self.username,
            "score": self.score
        }

        scores_list = []
        
        if os.path.exists(file_path):
            with open(file_path,'r') as file_json:
                try:
                    scores_list = json.load(file_json)

                    if not isinstance(scores_list, list):
                        scores_list = [scores_list]
                except json.JSONDecodeError:
                    scores_list = []

        user_found = False

        for entry in scores_list:
            if entry["username"] == self.username:
                user_found= True
                if self.score > entry["score"]:
                    entry["score"] = self.score
                break
        
        if not user_found:
            scores_list.append(new_score_entry)

        with open(file_path, 'w') as file_json:
            json.dump(scores_list, file_json, indent=4)

        print(f"\n--- {self.username}'s Final Score: {self.score}/{len(self.questions)} ---")
        print("\n🏆 Top 5 Highest Scorers 🏆")
        sorted_scores = sorted(scores_list, key=lambda x: x["score"], reverse=True)

        for i, entry in enumerate(sorted_scores[:5],start=1):
            print(f"{i}. {entry['username']} - {entry['score']}")
        



if __name__ == "__main__":
    questions = []
    try:
        with open("questions.json","r") as file:
            data = json.load(file)
            for i in data["questions"]:
                questions.append(Question(i["id"], i["text"],i["options"],i["answer"]))
    except FileNotFoundError:
        print("Error: The file 'questions.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file. Check for malformed JSON data.")
    

    quiz = QuizGame()
    quiz.add_question(questions)
    quiz.take_username()
    quiz.start_game()
    quiz.display_score()
