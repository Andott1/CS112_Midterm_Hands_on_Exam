import random


def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operation = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operation} {num2}"
    return question


def main():
    print("\n** WELCOME TO THE MATH BASIC OPERATION EXERCISE PROGRAM **\n")
    print("Note:\nRound answer to 2 decimal places.\nType 'exit' to end the program.\n")

    ques_count = 0

    while True:
        ques_count = ques_count + 1
        question = generate_question()
        user_answer = input(f"{ques_count}. What is the answer to {question}? ")

        if user_answer.lower() == 'exit':
            print("\nThank you for using the program! Have a great day!")
            break

        try:
            correct_answer = eval(question)
            user_answer = float(user_answer)
            correct_answer = round(correct_answer, 2)

            if user_answer == correct_answer:
                print("Correct! Well done!\n")
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}\n")
        except ValueError:
            print(f"Invalid input. Please enter a number or 'exit'.\n")


main()
