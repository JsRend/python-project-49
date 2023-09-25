import prompt

NUMBER_ROUND = 3


def greet_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def core(game):

    user_name = greet_user()
    print(f"{game.TASK}")

    COUNTER = 0

    while COUNTER < NUMBER_ROUND:

        question, correct_answer = game.make_question()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if user_answer.upper() == correct_answer.upper():

            print('Correct!')
            COUNTER += 1

        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'"
                f"\nLet's try again, {user_name}!"
            )
            return 0

    print(f'Congratulations, {user_name}!')
