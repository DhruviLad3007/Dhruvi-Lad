# Quiz Game in Python

def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. James Gosling",
                        "C. Guido van Rossum", "D. Elon Musk"],
            "answer": "C"
        },
        {
            "question": "Which of these is a programming language?",
            "options": ["A. HTML", "B. Python", "C. CSS", "D. All of these"],
            "answer": "D"
        },
        {
            "question": "What is 10 + 20?",
            "options": ["A. 20", "B. 25", "C. 30", "D. 40"],
            "answer": "C"
        }
    ]

    score = 0

    print("🎯 Welcome to the Quiz Game 🎯\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print("🏁 Quiz Finished")
    print(f"Your Final Score: {score}/{len(questions)}")


# Run the game
quiz_game()
