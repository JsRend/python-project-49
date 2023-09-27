import random

UPPER_BOUND = 50
LOWER_BOUND = 0

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():

    random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'no' if random_number % 2 else 'yes'

    return random_number, correct_answer
