import csv
import datetime
import logging

logging.basicConfig(filename="exam_client.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

CSV_FILE = "question.csv"

class ExamClient:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        try:
            with open(CSV_FILE, "r") as f:
                reader = csv.DictReader(f)
                self.questions = [row for row in reader]
            logging.info("Exam questions loaded.")
        except Exception as e:
            logging.error(f"Error loading exam questions: {e}")

    def conduct_exam(self, student_name, university):
        print("\n===== Online Exam =====")
        print("Date & Time:", datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S"))

        score = 0
        for q in self.questions:
            print(f"\nQ{q['num']}) {q['question']}")
            print(q["option1"].replace("=", ") "))
            print(q["option2"].replace("=", ") "))
            print(q["option3"].replace("=", ") "))
            print(q["option4"].replace("=", ") "))

            try:
                ans = input("Enter your choice (op1/op2/op3/op4): ").strip()
                if ans == q["correctoption"]:
                    score += 1
            except Exception:
                print("Invalid input. Skipping question.")

        print("\n===== Exam Result =====")
        print(f"Student Name: {student_name}")
        print(f"University  : {university}")
        print(f"Marks Scored: {score} correct out of {len(self.questions)}")

        logging.info(f"{student_name} from {university} scored {score}/{len(self.questions)}")


if __name__ == "__main__":
    name = input("Enter Student Name: ")
    university = input("Enter University: ")

    client = ExamClient()
    client.conduct_exam(name, university)
