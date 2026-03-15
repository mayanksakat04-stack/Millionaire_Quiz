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


if __name__ == "__main__":
    question1 = Question(
        1,
        "First human in space?",
        ["Yuri Gagarin", "Thomas Edison", "Albert Einstein"],
        1,
    )
    question2 = Question(
        2, "Who discovered gravity?", ["Tesla", "Einstein", "Isaac Newton"], 3
    )

    quiz = QuizGame()
    quiz.add_question([question1, question2])
    quiz.take_username()
    quiz.start_game()
    quiz.display_score()
