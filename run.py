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


user_name = introduction_func()


def game_difficult_selection():
    """
    Asks the user for input data on the basis of which the complexity
    of the game requested by the user is calculated
    """
    print(f'Hi {user_name}! First... choose the difficulty of the game')





