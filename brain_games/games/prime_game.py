import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def give_random_operand(lower_bound=2, upper_bound=100):
    return random.randint(lower_bound, upper_bound)


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def make_question():

    question = give_random_operand()
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
