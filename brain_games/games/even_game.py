import random

UPPER_BOUND = 50
LOWER_BOUND = 0

ANSWERS = {0: 'yes', 1: 'no'}

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():

    random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = (ANSWERS.get(random_number % 2))

    return random_number, correct_answer
