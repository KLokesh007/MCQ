import csv
import logging
import os

# Setup logger
logging.basicConfig(filename="question_master.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

CSV_FILE = "question.csv"

class QuestionMaster:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Load questions from CSV into nested data structure (list of dicts)."""
        if not os.path.exists(CSV_FILE):
            open(CSV_FILE, "w").close()

        try:
            with open(CSV_FILE, "r") as f:
                reader = csv.DictReader(f)
                self.questions = [row for row in reader]
            logging.info("Questions loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading questions: {e}")

    def save_questions(self):
        """Save questions back to CSV."""
        try:
            with open(CSV_FILE, "w", newline="") as f:
                fieldnames = ["num", "question", "option1", "option2", "option3", "option4", "correctoption"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.questions)
            logging.info("Questions saved successfully.")
        except Exception as e:
            logging.error(f"Error saving questions: {e}")

    def add_question(self, question, options, correct_option):
        num = str(len(self.questions) + 1)
        q_data = {
            "num": num,
            "question": question,
            "option1": f"op1={options[0]}",
            "option2": f"op2={options[1]}",
            "option3": f"op3={options[2]}",
            "option4": f"op4={options[3]}",
            "correctoption": f"op{correct_option}"
        }
        self.questions.append(q_data)
        self.save_questions()
        logging.info(f"Added question {num}")

    def search_question(self, num):
        for q in self.questions:
            if q["num"] == str(num):
                return q
        return None

    def delete_question(self, num):
        self.questions = [q for q in self.questions if q["num"] != str(num)]
        self.save_questions()
        logging.info(f"Deleted question {num}")

    def modify_question(self, num, new_data):
        for q in self.questions:
            if q["num"] == str(num):
                q.update(new_data)
                self.save_questions()
                logging.info(f"Modified question {num}")
                return
        logging.warning(f"Question {num} not found.")

    def display_all(self):
        for q in self.questions:
            print(q)


def menu():
    qm = QuestionMaster()
    while True:
        print("\n--- Question Master Menu ---")
        print("1. Add a Question")
        print("2. Search Question")
        print("3. Delete Question")
        print("4. Modify Question")
        print("5. Display All Questions")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if choice == 1:
            q = input("Enter question: ")
            opts = [input(f"Option {i+1}: ") for i in range(4)]
            correct = int(input("Correct option (1-4): "))
            qm.add_question(q, opts, correct)

        elif choice == 2:
            num = input("Enter question number: ")
            result = qm.search_question(num)
            print(result if result else "Not found.")

        elif choice == 3:
            num = input("Enter question number: ")
            qm.delete_question(num)

        elif choice == 4:
            num = input("Enter question number: ")
            q = input("New question: ")
            opts = [input(f"Option {i+1}: ") for i in range(4)]
            correct = int(input("Correct option (1-4): "))
            new_data = {
                "question": q,
                "option1": f"op1={opts[0]}",
                "option2": f"op2={opts[1]}",
                "option3": f"op3={opts[2]}",
                "option4": f"op4={opts[3]}",
                "correctoption": f"op{correct}"
            }
            qm.modify_question(num, new_data)

        elif choice == 5:
            qm.display_all()

        elif choice == 6:
            print("Exiting...")
            break


if __name__ == "__main__":
    menu()
