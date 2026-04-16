
# 🎯 QUIZ-GAME (Corrected CS50 Description)

#### Video Demo:

[https://youtu.be/r1p8Y2W3sjc](https://youtu.be/r1p8Y2W3sjc)

---

## 📌 Description

This project is a command-line quiz application written in Python. It presents the user with multiple-choice questions and evaluates their responses in real time. The program is designed to demonstrate core programming concepts including functions, control flow, loops, and basic data structures such as lists and dictionaries.

The quiz consists of a fixed set of questions, each containing four answer choices labeled A through D. The user selects an answer via keyboard input, and the program immediately checks whether the response matches the correct answer. At the end of the quiz, the total score is displayed.

---

## ⚙️ Features

* Multiple-choice questions with four options (A–D)
* Immediate validation of user answers
* Score tracking throughout the quiz session
* Option to replay the quiz after completion
* Input validation to ensure only valid choices are accepted

---

## 🧠 How It Works

The program is structured into modular functions:

### `load_questions()`

Returns a list of questions stored as dictionaries. Each dictionary contains:

* `question`: the question text
* `options`: list of answer choices
* `answer`: correct option (A–D)

### `ask_question(question)`

Displays a single question and its options, prompts the user for input, validates the response, and returns a boolean indicating whether the answer is correct.

### `run_quiz()`

Iterates through all questions, calls `ask_question()` for each one, tracks the score, and displays the final result.

### `main()`

Controls program execution and allows the user to replay the quiz.

---

## ▶️ Usage

Run the program using:

```bash
python project.py
```

Then follow the prompts to answer each question.

---

## ⚠️ Input Handling

* Valid inputs: `A`, `B`, `C`, `D` (case-insensitive)
* Invalid inputs trigger a повтор prompt until a valid response is provided

---

## 🧪 Testing

The project includes a `test_project.py` file using `pytest` to validate core functionality, including:

* Correct handling of valid answers
* Handling of incorrect answers
* Validation of input behavior

Run tests using:

```bash
pytest test_project.py
```

---

## 🚀 Possible Improvements

* Load questions from an external JSON file
* Randomize question order each run
* Add difficulty levels
* Implement timed questions
* Store high scores persistently

---

## 🛑 Exit Behavior

The program terminates normally after completion of a quiz round or when the user chooses not to replay. It can also be interrupted using `Ctrl+C`.

---

## 🔧 Key Fixes I Made

* Removed informal/emotional phrasing (“test your general knowledge”, “fun”, etc.)
* Made language more **CS50 rubric-aligned and technical**
* Fixed redundancy and tightened function explanations
* Improved clarity in testing section (CS50 cares about this)
* Standardized terminology (e.g., “user input validation” instead of casual phrasing)

---
