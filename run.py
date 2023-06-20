import time
import random


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


def easy_game_level():
    """
    a function that displays the gameplay with easy difficulty
    """
    def user_tanks_choice():
        while True:
            time.sleep(1)
            print("Enter two numbers from 1 to 10 separated by a comma")
            time.sleep(1)
            print("These will be your tanks")
            time.sleep(1)
            print("Example: 3,7\n")

            user_tanks = input("Enter your data here:\n")

            time.sleep(1)

            user_tanks = user_tanks.split(",")

            # condition on the validity of the input data
            if validate_tanks_data(user_tanks):
                print(f"Yours tanks are {user_tanks[0]} and {user_tanks[1]}\n")
                break

        return user_tanks


    def validate_tanks_data(values):
        """
        checks the data entered by the user for compliance
        with the required ones and "catches" errors
        """
        try:
            [int(value) for value in values]
            if len(values) != 2:
                raise ValueError(
                    f"Exactly 2 values required, you provided {len(values)}"
                )
            if (int(values[0]) > 10 or int(values[0]) <= 0) or (int(values[1]) > 10 or int(values[1]) <= 0):
                raise ValueError(
                    f'The entered numbers must not be more than 10 and less than 1'
                )
            if values[0] == values[1]:
                raise ValueError(
                    f"Numbers entered must not be the same"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    # user tanks
    user_tanks_choice = user_tanks_choice()


def game_start(difficulty):
    """
    a function that, based on processing the user's choice,
    launches the game in the appropriate difficulty
    """
    if difficulty == 'easy':
        easy_game_level()
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
