from models import Question
from game import QuizGame
import sqlite3
if __name__ == "__main__":
    questions = []
    try:
        conn = sqlite3.connect('quiz_data.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * from Questions
        """)
        rows = cursor.fetchall()

        for row in rows:
            q_id = row[0]
            q_text = row[1]
            q_opts = [row[opt] for opt in range(2,6)]
            q_answer = row[6]
            
            questions.append(Question(
                q_id,
                q_text,
                q_opts,
                q_answer
            ))

        print("Instance of Questions classes created via Database")
        # with open("questions.json","r") as file:
        #     data = json.load(file)
        #     for i in data["questions"]:
        #         questions.append(Question(i["id"], i["text"],i["options"],i["answer"]))
    except sqlite3.Error as error:
        print(f"SQL Error: {error}")

    quiz = QuizGame()
    quiz.add_question(questions)
    quiz.take_username()
    quiz.start_game()
    quiz.display_score()
