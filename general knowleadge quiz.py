QUESTIONS = [
    {
        "prompt": "How many elements are in the periodic table?",
        "options": ("A. 116", "B. 177", "C. 118", "D. 119"),
        "answer": "C",
    },
    {
        "prompt": "Which animal lays the largest eggs?",
        "options": ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
        "answer": "D",
    },
    {
        "prompt": "What is the most abundant gas in Earth's atmosphere?",
        "options": ("A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Hydrogen"),
        "answer": "A",
    },
    {
        "prompt": "How many bones are in the adult human body?",
        "options": ("A. 206", "B. 207", "C. 208", "D. 209"),
        "answer": "A",
    },
    {
        "prompt": "What planet in the solar system is the hottest?",
        "options": ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
        "answer": "B",
    },
    {
        "prompt": "What is the biggest planet in our solar system?",
        "options": ("A. Uranus", "B. Jupiter", "C. Mars", "D. Saturn"),
        "answer": "B",
    },
]


def normalize_answer(value):
    return value.strip().upper()


def is_valid_answer(value):
    return normalize_answer(value) in {"A", "B", "C", "D"}


def calculate_score(answers, questions=QUESTIONS):
    correct = 0
    for guess, question in zip(answers, questions):
        if normalize_answer(guess) == question["answer"]:
            correct += 1
    return correct, round((correct / len(questions)) * 100, 2)


def run_quiz(input_func=input):
    guesses = []
    for question in QUESTIONS:
        print("----------------------------")
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        while True:
            guess = input_func("Enter (A, B, C, D): ")
            if is_valid_answer(guess):
                break
            print("Please enter A, B, C, or D.")

        guess = normalize_answer(guess)
        guesses.append(guess)
        if guess == question["answer"]:
            print("CORRECT")
        else:
            print("INCORRECT")
            print(f"{question['answer']} is the correct answer")

    correct, percent = calculate_score(guesses)
    print("------------------")
    print("     RESULTS      ")
    print("------------------")
    print("Guesses:", " ".join(guesses))
    print(f"Correct answers: {correct}/{len(QUESTIONS)}")
    print(f"Your score is: {percent}%")


if __name__ == "__main__":
    run_quiz()
