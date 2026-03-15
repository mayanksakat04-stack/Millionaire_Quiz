import re

quiz = {
    1: {
        "question": "First human in space?",
        "options": ["Yuri Gagarin", "Thomas Edison", "Albert Einstein"],
        "answer": 1,
    },
    2: {
        "question": "Who discovered gravity?",
        "options": ["Tesla", "Einstein", "Isaac Newton"],
        "answer": 3,
    },
}

while True:
    try:
        user_input = input(
            "\nEnter username (alphanumeric): "
        )

        if re.match(r"^\w+$", user_input):
            print("Username accepted")
            break
        else:
            print("Username must be alphanumeric")
    except KeyboardInterrupt:
        print("\nExit")
        quit()

name = user_input
score = 0

for q, value in quiz.items():

    print(f"\n{q}. {value['question']}\n")

    for i, option in enumerate(value["options"], start=1):
        print(f"{i}. {option}")

    try:
        answer = int(input("Select option (0 to exit): "))

        if answer == 0:
            break

        if answer == value["answer"]:
            print("Correct!")
            score += 1
        else:
            correct = value["options"][value["answer"] - 1]
            print(f"Wrong! Correct answer: {correct}")

        print(f"{name}'s Score: {score}")

    except ValueError:
        print("Please enter a valid number")