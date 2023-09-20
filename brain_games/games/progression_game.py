import random

from brain_games.games.brain_engine import starting_game, greeting

min_length = 10
number_round = 3
step_border_min = 1
step_border_max = 6


def rand_operand(lower_bound=0, upper_bound=15):
    return random.randint(lower_bound, upper_bound)


def progression_game():
    user_name = greeting()
    print('What number is missing in the progression?')

    for count in range(int(number_round)):

        length_progression = rand_operand(min_length)
        initial_element = rand_operand()
        step_progression = rand_operand(step_border_min, step_border_max)

        progression_list = []
        last_elem = (initial_element + (step_progression * length_progression))

        for element in range(initial_element, last_elem, step_progression):
            progression_list.append(element)

        random_element = random.choice(progression_list)
        element_index = progression_list.index(random_element)
        correct_answer = progression_list.pop(element_index)

        patch = '..'
        progression_list.insert(element_index, patch)

        question = ' '.join(map(str, progression_list))

        if starting_game(question, correct_answer):
            continue
        else:
            return 0
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    progression_game()
