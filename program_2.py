# By Nathan Nelsen
# Written 20/2/2026
# Math Quiz

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

import random

def math_question(answer):
    answer = 0.0

    num1 = random.randint(1,999)
    num2 = random.randint(1,999)

    print("What is", num1, "plus", num2, "?")
    answer = float(input("Answer: "))

    correct_answer = num1 + num2

    if answer == correct_answer:
        print("Congratulations! That is correct!")
    else:
        print("Sorry, that's not correct.")
        print("The correct answer is:",correct_answer)

math_question(0)

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
