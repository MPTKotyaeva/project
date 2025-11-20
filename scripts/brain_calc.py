#!/usr/bin/env python3
import random

def main():
    print("VD-calc")
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])

        match operator:
            case '+':
                correct_answer = a + b
            case '-':
                correct_answer = a - b
            case '*':
                correct_answer = a * b

        print(f"Question: {a} {operator} {b}")
        user_answer = input("Your answer: ")

        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
