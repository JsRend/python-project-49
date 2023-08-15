import random

from brain_engine import starting_game, greeting

number_round = 3
upper_bound = 50
lower_bound = 0

answers = dict({0: 'yes', 1: 'no'})


def even_game():

    user_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for count in range(int(number_round)):
        random_number = random.randint(lower_bound, upper_bound)
        correct_answer = (answers.get(random_number % 2))
        if starting_game(random_number, correct_answer):
            continue
        else:
            return 0
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    even_game()
