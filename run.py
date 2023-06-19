import time


def introduction_func():
    """
    Displays a welcome message to the user with a description of the game,
    and also asks for a username
    """
    introduction = """
    Welcome to the tanks battle game!
    In this game, the one who quickly knocks out all the enemy tanks will win.
    Intrigued? Then let's get started...\n"""

    print(introduction)
    time.sleep(3)
    user = input('Enter your name or nickname\n')
    return user


# call introduction_func and write the return value to a variable
user_name = introduction_func()


def game_difficulty_selection():
    """
    Asks the user for input data on the basis of which the complexity
    of the game requested by the user is calculated
    """
    print()
    print(f'Hi {user_name}! First... choose the difficulty of the game')
    time.sleep(2)
    print('Enter a number from 1 to 3, where 3 is the highest difficulty\n')
    choice = input()

    while choice != '1' and choice != '2' and choice != '3':
        print('Incorrect data entered. Enter a number from 1 to 3')
        choice = input()
    return choice


# call game_difficulty_selection and write the return value to a variable
user_choice = game_difficulty_selection()


def check_difficulty():
    """
    Based on the data entered by the user,
    the function sets the game difficulty value
    """
    if int(user_choice) == 1:
        level = 'easy'
    elif int(user_choice) == 2:
        level = 'medium'
    else:
        level = 'hard'
    return level


# call check_difficulty and write the return value to a variable
pick_user_level_game = check_difficulty()


def game_start(difficulty):
    """
    a function that, based on processing the user's choice,
    launches the game in the appropriate difficulty
    """
    if difficulty == 'easy':
        print('easy')
    elif difficulty == 'medium':
        print('medium')
    else:
        print('hard')


def main():
    """
    the main function that launches the game process
    """
    game_start(pick_user_level_game)


# call main to start the game
main()
