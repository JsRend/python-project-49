import random

UPPER_BOUND = 50
LOWER_BOUND = 1

TASK = 'Find the greatest common divisor of given numbers.'


def give_random_operand():
    return random.randint(LOWER_BOUND, UPPER_BOUND)


def find_gcd(number_a, number_b):

    if number_a < number_b:
        smaller_num, larger_num = number_a, number_b
    else:
        smaller_num, larger_num = number_b, number_a

    while True:
        remainder = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = remainder
        if remainder == 0:
            break

    return larger_num


def make_question():

    number_a = give_random_operand()
    number_b = give_random_operand()

    question = f"{number_a} {number_b}"
    correct_answer = f"{find_gcd(number_a, number_b)}"

    return question, correct_answer
