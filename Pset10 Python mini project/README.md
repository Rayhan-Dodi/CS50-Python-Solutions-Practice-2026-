
# 🎯 QUIZ-GAME

#### Video Demo: 👀

#### Description:

This project is a Python-based command-line quiz game designed to test the user’s general knowledge through a series of multiple-choice questions. The application focuses on fundamental programming concepts such as control flow, data structures, and user interaction, making it suitable for beginners and aligned with CS50 Python project standards.

The program presents a sequence of questions, each with four possible answers labeled A through D. The user selects an answer via keyboard input, and the program immediately evaluates whether the response is correct. At the end of the quiz, the total score is displayed.

---

## ⚙️ Features

* 📋 Multiple-choice questions with 4 options each
* ✅ Immediate feedback (correct / incorrect)
* 🎯 Score tracking system
* 🔁 Replay functionality
* ⚠️ Input validation to prevent invalid entries

---

## 🧠 How It Works

The program is structured into modular functions:

* `load_questions()`
  Returns a list of questions stored as dictionaries. Each question contains:

  * question text
  * options list
  * correct answer

* `ask_question(question)`
  Displays a single question, takes user input, validates it, and returns whether the answer is correct.

* `run_quiz()`
  Iterates through all questions, tracks score, and prints results.

* `main()`
  Controls the game loop and allows replay.

---

## ▶️ Usage

Run the program from the command line:

```bash
python project.py
```

Follow on-screen instructions to answer each question.

---

## ⚠️ Input Handling

* Accepts only: `A`, `B`, `C`, `D` (case-insensitive)
* Invalid inputs will prompt the user to try again

---

## 🧪 Testing

The project includes a `test_project.py` file using `pytest` to verify:

* Question structure validity
* Correct answer handling
* Incorrect answer handling
* Input validation behavior

Run tests using:

```bash
pytest test_project.py
```

---

## 🚀 Possible Improvements

* 📂 Load questions dynamically from a JSON file
* ⏱ Add time limits per question
* 📊 Store high scores persistently
* 🎮 Add difficulty levels
* 🔀 Randomize question order

---

## 🛑 Exit Behavior

The program can be exited normally after a quiz session or interrupted using `Ctrl+C`, which will terminate execution.

---
