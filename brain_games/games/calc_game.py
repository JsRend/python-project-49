import random

from brain_games.games.brain_engine import starting_game, greeting

NUMBER_ROUND = 3
UPPER_BOUND = 50
LOWER_BOUND = 0

OPERATIONS = dict({0: '+', 1: '-', 2: '*'})


def rand_operand():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def calc_game():

    user_name = greeting()

    print('What is the result of the expression?')

    for count in range(int(NUMBER_ROUND)):

        random_operation = OPERATIONS.get(random.choice(list(OPERATIONS)))
        question = f"{rand_operand()} {random_operation} {rand_operand()}"
        correct_answer = f"{eval(question)}"

        if starting_game(question, correct_answer, user_name):
            continue
        else:
            return 0

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    calc_game()
