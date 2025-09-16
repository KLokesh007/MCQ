# MCQ Based Online Exam Application

This project is a simple MCQ (Multiple Choice Question) Online Exam Application built in Python.
It includes two main modules:

question_master.py → Manage questions (Add, Search, Modify, Delete, Display).

exam_client.py → Conduct exams for students and display results.

Questions are stored in a CSV file (question.csv) for persistence.

# Question Master (question_master.py)

Add a new question (auto-numbered).

Search a question by its number.

Delete a question by its number.

Modify an existing question.

Display all questions in the system.

Stores data in question.csv.

Logs actions in question_master.log.

# Exam Client (exam_client.py)

Displays current date & time.

Collects student details (name & university).

Displays each question with options.

Accepts user answer (op1–op4 or 1–4).

Calculates & displays the final score.

Logs exam results in exam_client.log.


# Project Structure

mcq_exam/
│
├── question.csv          # Stores all questions
├── question_master.py    # Question management system
├── exam_client.py        # Exam interface for students
├── question_master.log   # Log file for question operations
├── exam_client.log       # Log file for exam sessions
└── README.md             # Project documentation

# Requirements

Python 3.8+

Works on Windows, macOS, and Linux

No external dependencies (only Python standard libraries used: csv, logging, datetime)