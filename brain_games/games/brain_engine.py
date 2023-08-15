import prompt


def greeting():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def task_player(user_task):
    print(f"Question: {user_task}")


def successful_execution():
    print('Correct!')


def execution_with_error(user_answer, correct_answer):
    print(
        f"'{user_answer}' is wrong answer ;(."
        f" Correct answer was '{correct_answer}'"
        )


def starting_game(question, correct_answer):

    task_player(question)
    user_answer = prompt.string('Your answer: ')
    if user_answer.upper() == correct_answer.upper():
        successful_execution
    else:
        execution_with_error(user_answer, correct_answer)
        return 0
