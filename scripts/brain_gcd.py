#!/usr/bin/env python3
import random
import math

def main():
    print("VD-gcd")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct_answer = math.gcd(a, b)

        print(f"Question: {a} {b}")
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
