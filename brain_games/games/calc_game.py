import random

from brain_games.games.brain_engine import starting_game, greeting

number_round = 3
count_operand = 2
operands = []
upper_bound = 50
lower_bound = 0

operations = dict({0: '+', 1: '-', 2: '*'})


def rand_operand():
    return random.randint(lower_bound, upper_bound)


def calc_game():

    user_name = greeting()
    print('What is the result of the expression?')

    for count in range(int(number_round)):
        random_operation = operations.get(random.choice(list(operations)))
        question = f"{rand_operand()} {random_operation} {rand_operand()}"
        correct_answer = f"{eval(question)}"

        if starting_game(question, correct_answer):
            continue
        else:
            return 0
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    calc_game()
