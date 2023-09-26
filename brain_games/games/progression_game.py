import random

MIN_LENGTH = 10
STEP_BORDER_MAX = 6
STEP_BORDER_MIN = 1

TASK = 'What number is missing in the progression?'


def give_random_operand(lower_bound=0, upper_bound=15):
    return random.randint(lower_bound, upper_bound)


def make_question():

    length_progression = give_random_operand(MIN_LENGTH)
    initial_element = give_random_operand()
    step_progression = give_random_operand(STEP_BORDER_MIN, STEP_BORDER_MAX)

    progression_list = []
    last_elem = (initial_element + (step_progression * length_progression))

    for element in range(initial_element, last_elem, step_progression):
        progression_list.append(element)

    random_index = random.randrange(0, length_progression)
    correct_answer = str(progression_list[random_index])

    progression_list[random_index] = '..'

    question = ' '.join(map(str, progression_list))
    # map(str, LIST) allows you to remove the quotation marks "[" when output.
    # Not a bug, a feature

    return question, correct_answer
