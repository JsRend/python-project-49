import random
import operator

UPPER_BOUND = 50
LOWER_BOUND = 0

OPERATIONS = {0: '+', 1: '-', 2: '*'}

TASK = 'What is the result of the expression?'


def give_random_operand():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def get_correct_answer(question: str):
    components = question.split()
    if components[1] == '+':
        return operator.add(int(components[0]), int(components[2]))
    if components[1] == '-':
        return operator.sub(int(components[0]), int(components[2]))
    if components[1] == '*':
        return operator.mul(int(components[0]), int(components[2]))


def make_question():

    random_operation = random.choice(OPERATIONS)
    question = (f"{give_random_operand()}"
                f" {random_operation} "
                f"{give_random_operand()}"
                )

    correct_answer = f"{get_correct_answer(question)}"

    return question, correct_answer
