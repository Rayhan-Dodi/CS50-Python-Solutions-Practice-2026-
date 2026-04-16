def load_questions():
    return [
        {
            "question": "What is the capital of Bangladesh?",
            "options": ["A. Dhaka", "B. Chittagong", "C. Khulna", "D. Sylhet"],
            "answer": "A"
        },
        {
            "question": "Which language is used in CS50?",
            "options": ["A. Python", "B. C", "C. JavaScript", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Process Unit",
                "B. Central Processing Unit",
                "C. Computer Personal Unit",
                "D. Central Performance Unit"
            ],
            "answer": "B"
        }
    ]


def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer == q["answer"]
        else:
            print("Invalid input. Try again.")


def run_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        if ask_question(q):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print(f"\n🎯 Your score: {score}/{len(questions)}")


def main():
    while True:
        run_quiz()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()