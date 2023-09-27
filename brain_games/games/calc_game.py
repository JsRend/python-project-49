import random
from operator import add, mul, sub

UPPER_BOUND = 50
LOWER_BOUND = 0

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul
}

TASK = 'What is the result of the expression?'


def give_random_operand():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def make_question():

    random_operation = random.choice(list(OPERATIONS))

    question = (f"{give_random_operand()}"
                f" {random_operation} "
                f"{give_random_operand()}"
                )
    components = question.split()

    correct_answer = str(
        OPERATIONS[random_operation]
        (int(components[0]), int(components[2]))
    )

    return question, correct_answer
