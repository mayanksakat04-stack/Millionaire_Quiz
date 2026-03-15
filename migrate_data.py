import sqlite3
import json

def migrate_data():
    try:
        conn = sqlite3.connect('quiz_data.db')
        cursor = conn.cursor()

        with open('questions.json','r') as file:
            data = json.load(file)

            for question in data["questions"]:
                q_text = question["text"]
                q_opt1 = question["options"][0]
                q_opt2 = question["options"][1]
                q_opt3 = question["options"][2]
                q_opt4 = question["options"][3]
                q_answer = question["answer"]

                insert_query = """
                    INSERT INTO Questions(question_text, option_A, option_B, option_C, option_D, answer)
                    VALUES (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(insert_query, (q_text, q_opt1 ,q_opt2 ,q_opt3 ,q_opt4, q_answer))
        conn.commit()
        conn.close()
        print("Data successfully migrated from JSON to SQLite3")
    except sqlite3.Error as error:
        print(f"Database Error: {error}")
    except FileNotFoundError:
        print("Error: JSON file not found")
    except json.JSONDecodeError:
        print("Unable to Decode JSON file")
    except IndexError as error:
        print(f"List Index Error: {error}. Check if your lists have enough items!")

if __name__ == "__main__":
    migrate_data()