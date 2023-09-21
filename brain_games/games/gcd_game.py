import random

from brain_games.games.brain_engine import starting_game, greeting

NUMBER_ROUND = 3
UPPER_BOUND = 50
LOWER_BOUND = 0


def rand_operand():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def find_gcd(larger_num, smaller_num):

    if larger_num and smaller_num == 0:
        return 0

    if larger_num < smaller_num:
        larger_num, smaller_num = smaller_num, larger_num

    while True:
        remainder = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = remainder
        if remainder == 0:
            break

    return larger_num


def gcd_game():

    user_name = greeting()

    print('Find the greatest common divisor of given numbers.')

    for count in range(int(NUMBER_ROUND)):

        number_a = rand_operand()
        number_b = rand_operand()

        question = f"{number_a} {number_b}"
        correct_answer = f"{find_gcd(number_a, number_b)}"

        if starting_game(question, correct_answer, user_name):
            continue
        else:
            return 0

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    gcd_game()
