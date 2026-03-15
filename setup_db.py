import sqlite3

def setup_database():
    try:
        conn = sqlite3.connect('quiz_data.db')
        cursor = conn.cursor()

        create_questions_table = """
        CREATE TABLE IF NOT EXISTS Questions(
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text VARCHAR(300) NOT NULL,
            option_A VARCHAR(100) NOT NULL,
            option_B VARCHAR(100) NOT NULL,
            option_C VARCHAR(100) NOT NULL,
            option_D VARCHAR(100) NOT NULL,
            answer INTEGER NOT NULL
        )
        """

        create_users_table = """
        CREATE TABLE IF NOT EXISTS Users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100) NOT NULL
        )
        """

        create_score_table = """
        CREATE TABLE IF NOT EXISTS Scores(
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        top_score INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
        """

        cursor.execute(create_questions_table)
        cursor.execute(create_users_table)
        cursor.execute(create_score_table)

        conn.commit()
        conn.close()

        print("Databases and tables created successfully.")
    except sqlite3.Error as error:
        print(f"Falied to create tables: {error}")

if __name__ == "__main__":
    setup_database()