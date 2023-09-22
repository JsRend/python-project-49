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


def execution_with_error(user_answer, correct_answer, user_name):
    print(
        f"'{user_answer}' is wrong answer ;(."
        f" Correct answer was '{correct_answer}'"
        f"\nLet's try again, {user_name}!"
        )


def starting_game(question, correct_answer, name):

    task_player(question)
    user_answer = prompt.string('Your answer: ')
    try:
        if user_answer.upper() == correct_answer.upper():
            successful_execution()
            return True
        else:
            execution_with_error(user_answer, correct_answer, name)
            return False
    except AttributeError:
        if int(user_answer) == int(correct_answer):
            successful_execution()
            return True
        else:
            execution_with_error(user_answer, correct_answer, name)
            return False
