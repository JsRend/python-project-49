import prompt
import random

number_round = 3
upper_bound = 50
lower_bound = 0

answers = dict({0: 'yes', 1: 'no'})


def even_game():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for round in range(int(number_round)):
        random_number = random.randint(lower_bound, upper_bound)
        print(f"Question: {random_number}")
        correct_answer = (answers.get(random_number % 2))

        user_answer = prompt.string('Your answer: ')
        if user_answer.upper() == correct_answer.upper():
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'"
                )
            return 0

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    even_game()
