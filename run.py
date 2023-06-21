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
                    'The entered numbers must not be more than 10 and less than 1'
                )
            if values[0] == values[1]:
                raise ValueError(
                    "Numbers entered must not be the same"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    # user tanks
    user_tanks_choice = user_tanks_choice()

    # computer possible tanks list
    computer_possible_tanks_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    # computer tanks
    computer_tanks = []

    def computer_tanks_choice(list):
        """
        A function that determines the computer's tanks
        by choosing a random number from a given list
        """
        time.sleep(2)
        print('And now the computer makes its choice... wait a second')
        time.sleep(2)
        print('The computer has only 1 tank')
        time.sleep(2)
        computer_tanks = random.randint(1, len(list) - 1)
        print('The computer has made its choice\n')

        return computer_tanks

    computer_tanks.append(str(computer_tanks_choice(computer_possible_tanks_list)))
    # print(computer_tanks)
    # print(type(computer_tanks[0]))
    # time.sleep(2)

    """
    variables that are needed for the life cycle of the game
    """
    # user maded moves
    user_maded_moves = []
    # user_possible_moves
    user_possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def user_move(maded_moves, possible_moves):
        """The function describes the process of firing a shot, validates the data entered by the user, adds the user's move to the variable and removes the values entered by the user from the possible moves"""
        print()
        print('User turn')
        print(f'Your attempts: {maded_moves}')
        print(f'Possible moves: {possible_moves}')
        print(f'Your tanks: {user_tanks_choice}')
        print('Where do you order to shoot sir/ma\'am?')
        while True:
            user_shot = input('Enter a number from 1 to 10\n')
            print()
            
            if validate_user_shot(user_shot):
                print('Fire!\n')
                maded_moves.append(user_shot)
                possible_moves.remove(int(user_shot))
                time.sleep(2)
                print(user_shot)
                print(maded_moves)
                print(possible_moves)
                break
    
    def validate_user_shot(value):
        """
        the function validates the data entered by the user and handles possible errors
        """
        try:
            if int(value) > 10:
                raise ValueError(
                    "The entered number must not be more than 10"
                )
            if  int(value) < 1:
                raise ValueError(
                    "The entered number must not be less than 1"
                )
            if  value in user_maded_moves:
                raise ValueError(
                    "You have already entered this value. Choose another"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    def first_move_choice():
        """
        The function randomly selects one of two values
        that determines who will go first
        """
        time.sleep(2)
        print("Now let's decide who will go first.")
        time.sleep(2)
        print('Flipping a coin... ')
        time.sleep(2)
        print('And...\n')
        time.sleep(2)
        if random.randint(0, 1) == 0:
            print('You are lucky! You go first\n')
            return 'user'
        else:
            print('You are unlucky...:( The computer goes first\n')
            return 'computer'

    # first_move_choice
    first_move = first_move_choice()

    def game_cycle(moveChoice):
        """
        A function that deduces the rules of the game and
        triggers the life cycle of the game based on who goes first.
        """
        time.sleep(2)
        print('Just a second... I will briefly talk about the rules of the game and begin\n')
        time.sleep(2)
        print('The player and the computer take turns shooting at enemy tanks')
        time.sleep(2)
        print(f'Enter a new number each time between 1 and {len(computer_possible_tanks_list)}')
        time.sleep(2)
        print('If there is an enemy tank in the number entered by the user or selected by the computer, it is hit')
        time.sleep(2)
        print('The winner is the one who quickly knocks out all the enemy tanks\n')
        time.sleep(2)
        print('And now let\'s start...\n')
        time.sleep(2)
        print(f'Goes first {moveChoice}')

        if moveChoice == 'user':
            user_move(user_maded_moves, user_possible_moves)
        else:
            print('Computer goes first')

    game_cycle(first_move)


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
