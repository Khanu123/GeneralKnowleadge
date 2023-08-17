questions = ("How many elements are in the periodic table?: ",
"Which animal lays the largest eggs?: ",
"What is the most abundent gas in Earth's atmosphere?:",
"How many bones are in the human body?:",
"What planet in the solar system is the hottest?:",
"What is the biggest planet in our solar system?:",)


options = (("A. 116", "B. 177", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Uranus", "B. Jupiter", "C. Mars", "D. Saturn"))


answers = ("C", "D", "A", "A", "B", "B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("----------------------------")
    print (question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRENT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("------------------")
print("     RESUTLS      ")
print("------------------")


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) *100)
print(f"Your score is : {score}%")

