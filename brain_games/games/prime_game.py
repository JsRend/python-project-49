import random

from brain_games.games.brain_engine import starting_game, greeting

NUMBER_ROUND = 3


def rand_operand(lower_bound=2, upper_bound=100):
    return random.randint(lower_bound, upper_bound)


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return 'no'
    return 'yes'


def prime_game():

    user_name = greeting()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for count in range(int(NUMBER_ROUND)):

        number = rand_operand()
        correct_answer = is_prime(number)
        question = number

        if starting_game(question, correct_answer, user_name):
            continue
        else:
            return 0

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    prime_game()
