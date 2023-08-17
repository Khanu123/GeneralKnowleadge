# GeneralKnowleadge
Setting up the Questions, Options, and Answers:

questions: This is a tuple containing the quiz questions.
options: This is a tuple of tuples, where each inner tuple contains the multiple-choice options for a specific question.
answers: This is a tuple containing the correct answers corresponding to each question.
Initializing Variables:

guesses: This list will store the user's guessed answers for each question.
score: This variable will keep track of the user's score.
question_num: This variable will be used to iterate through the questions and their options.
Quiz Loop:
The code enters a loop that goes through each question:

It prints the question.
It loops through the options for that question and prints them.
It asks the user to enter their choice ("A", "B", "C", or "D").
It converts the user's input to uppercase.
It appends the user's guess to the guesses list.
Checking Answers:

If the user's guess matches the correct answer (answers[question_num]), the user's score increases by 1, and "CORRECT" is printed.
If the user's guess is incorrect, "INCORRECT" is printed, along with the correct answer.
Updating question_num:
The question_num is incremented after each question, allowing the code to move to the next question in the loop.

Printing Results:

The code prints a divider and "RESULTS".
It prints the user's guesses for each question.
It calculates the user's percentage score and prints it.
This code demonstrates several programming concepts:

Looping: The code uses a loop to go through each question and its options.
User Input: The code prompts the user for input and processes it.
Conditional Statements: The code checks whether the user's guess is correct and responds accordingly.
Lists and Tuples: The code uses lists and tuples to store questions, options, guesses, and answers.
String Formatting: The code uses string formatting to display results and messages.
In summary, the code simulates a simple quiz game, where users answer multiple-choice questions, and their score is calculated and displayed at the end. It's a good example of using basic programming constructs to create an interactive quiz experience.
