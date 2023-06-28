import time
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tanksbattle')

logins = SHEET.worksheet('logins')
passwords = SHEET.worksheet('passwords')

# welcome image
print("              ||||||||    ")
time.sleep(0.4)
print("            |||||||||||")
time.sleep(0.4)
print("           |||||||||||||||||||||||||     |+| ")
time.sleep(0.4)
print("       ||||||||||||||||||")
time.sleep(0.4)
print("       |||||||||||||||||||||||")
time.sleep(0.4)
print("       |||||||||||||||||||||||")
time.sleep(0.4)
print("       |||||||||||||||||||||||")
time.sleep(0.5)


def check_user():
    """
    The function checks if the user is a registered user or not
    and receives data from the user
    """
    print()
    print("""The game has the right to accept only users
    who have passed the preliminary free registration\n""")
    time.sleep(2)
    print('Have you already registered?\n')
    user_registration_answer = input("Enter Y or N\n").lower()

    if user_registration_answer == 'y':
        signup()
    elif user_registration_answer == 'n':
        new_user_registration()
    else:
        print('Incorrect data entered. Enter Y or N\n')
        check_user()

    return user_registration_answer


def signup():
    """
    The function through which registered users are logged in
    """
    print()
    print("""To gain access to the game,
    please enter your login and password\n""")
    time.sleep(2)
    print()
    # input login
    login = input("Enter your login\n")

    # google sheets login check
    if (logins.find(login)) is None:
        print('Login you entered is missing\n')
        check_user()

    print()
    # input password
    password = input("Enter your password\n")

    # password sheets login check
    if (passwords.find(password)) is None:
        print('Password you entered is missing\n')
        check_user()


def new_user_registration():
    """
    The function of which is the registration of a new user
    """
    print('For free registration on the site, create a login and password')
    time.sleep(2)
    print()
    while True:
        print('\nEnter your login')
        print()
        new_login = input()
        print()
        print('Enter your password')
        new_password = input()

        registration_data = check_registration_data(new_login, new_password)

        if registration_data:
            # add login to google sheets
            logins.append_row(new_login.split())
            # add password to google sheets
            passwords.append_row(new_password.split())
            # variable converting username to greeting
            new_login_str = ''.join(new_login.split())
            print()
            time.sleep(1)
            print(f'Hi {new_login_str}')
            print("""Your password and login are saved.
            Now you need to use them to login to the game""")
            # function call  signup
            signup()
            break


def check_registration_data(new_login, new_password):
    try:
        if len(new_login) < 4 or len(new_password) < 4:
            raise ValueError(
                "login and password should be more than 4 characters"
            )
        if (logins.find(new_login)):
            raise ValueError(
                "this login already exists"
            )
        if ' ' in new_login or ' ' in new_password:
            raise ValueError(
                "spaces in login and password are not allowed"
            )
    except ValueError as e:
        print(f"Invalid input: {e}")
        return False
    else:
        print("\nThank you for registering....")
        time.sleep(1)
        return True


# function call  check_user
check_user()


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


# call introduction_func
introduction_func()


def game_difficulty_selection():
    """
    Asks the user for input data on the basis of which the complexity
    of the game requested by the user is calculated
    """
    print()
    print('First... choose the difficulty of the game')
    time.sleep(2)
    print('Enter a number from 1 to 3, where 3 is the highest difficulty\n')
    choice = input()

    while choice != '1' and choice != '2' and choice != '3':
        print('Incorrect data entered. Enter a number from 1 to 3')
        choice = input()
    return choice


# call game_difficulty_selection and write the return value to a variable
user_choice = game_difficulty_selection()


def check_difficulty(user_choice_difficulty):
    """
    Based on the data entered by the user,
    the function sets the game difficulty value
    """
    if int(user_choice_difficulty) == 1:
        level = 'easy'
    elif int(user_choice_difficulty) == 2:
        level = 'medium'
    else:
        level = 'hard'
    return level


# call check_difficulty and write the return value to a variable
pick_user_level_game = check_difficulty(user_choice)


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
            if (
                int(values[0]) > 10 or int(values[0]) <= 0
                ) or (
                    int(values[1]) > 10 or int(values[1]) <= 0
                    ):
                raise ValueError("""The entered numbers must not be
                more than 10 and less than 1""")
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
    computer_possible_tanks_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
        ]

    # computer tanks
    computer_tanks = []

    def computer_tanks_choice(list_computer_tanks_choice):
        """
        A function that determines the computer's tanks
        by choosing a random number from a given list
        """
        time.sleep(2)
        print('And now the computer makes its choice... wait a second')
        time.sleep(2)
        print('The computer has only 1 tank')
        time.sleep(2)
        computer_tanks = random.randint(1, len(list_computer_tanks_choice) - 1)
        print('The computer has made its choice\n')

        return computer_tanks

    computer_tanks.append(
        str(computer_tanks_choice(computer_possible_tanks_list))
        )

    # user maded moves
    user_maded_moves = []
    # user_possible_moves
    user_possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # computer moves
    computer_moves = []

    def user_move(maded_moves, possible_moves):
        """The function describes the process of firing a shot, validates
        the data entered by the user, adds the user's move to the variable
        and removes the values entered by the user from the possible moves"""
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
                break

    def validate_user_shot(value):
        """
        the function validates the data entered by the user
        and handles possible errors
        """
        try:
            if int(value) > 10:
                raise ValueError(
                    "The entered number must not be more than 10"
                )
            if int(value) < 1:
                raise ValueError(
                    "The entered number must not be less than 1"
                )
            if value in user_maded_moves:
                raise ValueError(
                    "You have already entered this value. Choose another"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    def shuffle_computer_move(list_for_shuffle_computer_move):
        """
        A function that generates a list of random possible computer moves
        """
        random.shuffle(list_for_shuffle_computer_move)
        shuffle = []
        for i in list_for_shuffle_computer_move:
            shuffle.append(i)

        return shuffle

    def computer_move(list_for_computer_move):
        """
        A function that plays a computer shot and
        writes its shot to the corresponding variable
        """
        print()
        time.sleep(1)
        print('Computer turn')
        time.sleep(2)
        print('He shoots straight...')

        for value in list_for_computer_move:
            if value in computer_moves:
                continue
            else:
                computer_moves.append(str(value))
                print(value)
                time.sleep(2)
                break

    # computer shuffle move
    shuffle_computer_move = shuffle_computer_move(computer_possible_tanks_list)

    def check_user_hit_the_target(shot, list_for_check_user_hit_the_target):
        """
        a function that checks if the user is in the tank
        """
        print('Checking if you hit the tank\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_for_check_user_hit_the_target:
            print('Exactly! You knocked out an enemy tank\n')
            list_for_check_user_hit_the_target.remove(shot[index])
            time.sleep(2)
        else:
            print('Miss ): Maybe you should aim better next time?\n')
            time.sleep(2)

    def check_computer_hit_the_target(shot, list_check_computer_hit_target):
        """
        a function that checks if the computer got into the user's tank
        """
        print('Checking if the computer hit the target\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_check_computer_hit_target:
            print('Damn! He knocked out your tank\n')
            list_check_computer_hit_target.remove(shot[index])
            time.sleep(2)
        else:
            print('Ha-ha! Computer missed\n')
            time.sleep(2)

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
        game = True
        time.sleep(2)
        print("""Just a second... I will briefly talk about the rules
        of the game and begin\n""")
        time.sleep(3)
        print('The player and the computer take turns shooting at enemy tanks')
        time.sleep(3)
        print(f"""Enter a new number each time between 1
        and {len(computer_possible_tanks_list)}""")
        time.sleep(3)
        print("""If there is an enemy tank in the number
        entered by the user or selected by the computer, it is hit""")
        time.sleep(3)
        print("""The winner is the one who quickly
        knocks out all the enemy tanks\n""")
        time.sleep(3)
        print('And now let\'s start...\n')
        time.sleep(2)

        if moveChoice == 'user':
            while game:
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
        else:
            while game:
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
        print()
        print('Game Over')
        time.sleep(2)

    game_cycle(first_move)
    # return new_game


def medium_game_level():
    """
    a function that displays the gameplay with easy difficulty
    """
    def user_tanks_choice():
        while True:
            time.sleep(1)
            print("Enter three numbers from 1 to 20 separated by a comma")
            time.sleep(1)
            print("These will be your tanks")
            time.sleep(1)
            print("Example: 3,10,14\n")

            user_tanks = input("Enter your data here:\n")

            time.sleep(1)

            user_tanks = user_tanks.split(",")

            # condition on the validity of the input data
            if validate_tanks_data(user_tanks):
                print(f"""Yours tanks are:
                {user_tanks[0]} and {user_tanks[1]} and {user_tanks[2]}\n""")
                break

        return user_tanks

    def validate_tanks_data(values):
        """
        checks the data entered by the user for compliance
        with the required ones and "catches" errors
        """
        try:
            [int(value) for value in values]
            if len(values) != 3:
                raise ValueError(
                    f"Exactly 3 values required, you provided {len(values)}"
                )
            if (
                int(values[0]) > 20 or int(values[0]) <= 0
                ) or (
                    int(values[1]) > 20 or int(values[1]) <= 0
                    ) or (
                        int(values[2]) > 20 or int(values[2]) <= 0
                        ):
                raise ValueError("""The entered numbers
                must not be more than 10 and less than 1""")
            if (
                values[0] == values[1] or
                values[0] == values[2] or
                values[1] == values[2]
               ):
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
    computer_possible_tanks_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
        ]

    # computer tanks
    computer_tanks = []

    def computer_tanks_choice(list_comp_tanks_medium):
        """
        A function that determines the computer's tanks
        by choosing a random number from a given list
        """
        time.sleep(2)
        print('And now the computer makes its choice... wait a second')
        time.sleep(2)
        print('The computer has 3 tank')
        time.sleep(2)
        computer_tanks_list = []
        while len(computer_tanks_list) != 3:
            for i in list_comp_tanks_medium:
                if i in computer_tanks_list:
                    continue
                else:
                    i = random.randint(1, len(list_comp_tanks_medium) - 1)
                    computer_tanks_list.append(str(i))
                    time.sleep(1)
                    break
        print('The computer has made its choice\n')
        return computer_tanks_list

    computer_tanks = (
        computer_tanks_choice(computer_possible_tanks_list)
        ).copy()

    # user maded moves
    user_maded_moves = []
    # user_possible_moves
    user_possible_moves = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20
        ]
    # computer moves
    computer_moves = []

    def user_move(maded_moves, possible_moves):
        """The function describes the process of firing a shot,
        validates the data entered by the user,
        adds the user's move to the variable
        and removes the values entered by the user from the possible moves"""
        print()
        print('User turn')
        print(f'Your attempts: {maded_moves}')
        print(f'Possible moves: {possible_moves}')
        print(f'Your tanks: {user_tanks_choice}')
        print('Where do you order to shoot sir/ma\'am?')
        while True:
            user_shot = input('Enter a number from 1 to 20\n')
            print()

            if validate_user_shot(user_shot):
                print('Fire!\n')
                maded_moves.append(user_shot)
                possible_moves.remove(int(user_shot))
                time.sleep(2)
                break

    def validate_user_shot(value):
        """
        the function validates the data entered by the user
        and handles possible errors
        """
        try:
            if int(value) > 20:
                raise ValueError(
                    "The entered number must not be more than 20"
                )
            if int(value) < 1:
                raise ValueError(
                    "The entered number must not be less than 1"
                )
            if value in user_maded_moves:
                raise ValueError(
                    "You have already entered this value. Choose another"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    def shuffle_computer_move(list_shuf_comp_move_medium):
        """
        A function that generates a list of random possible computer moves
        """
        random.shuffle(list_shuf_comp_move_medium)
        shuffle = []
        for i in list_shuf_comp_move_medium:
            shuffle.append(i)

        return shuffle

    def computer_move(list_comp_mov_medium):
        """
        A function that plays a computer shot and
        writes its shot to the corresponding variable
        """
        print()
        time.sleep(1)
        print('Computer turn')
        time.sleep(2)
        print('He shoots straight...')

        for value in list_comp_mov_medium:
            if value in computer_moves:
                continue
            else:
                print(value)
                computer_moves.append(str(value))
                time.sleep(1)
                break

    # computer shuffle move
    shuffle_computer_move = shuffle_computer_move(computer_possible_tanks_list)

    def check_user_hit_the_target(shot, list_user_hit_target_medium):
        """
        a function that checks if the user is in the tank
        """
        print('Checking if you hit the tank\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_user_hit_target_medium:
            print('Exactly! You knocked out an enemy tank\n')
            list_user_hit_target_medium.remove(shot[index])
            time.sleep(2)
        else:
            print('Miss ): Maybe you should aim better next time?\n')
            time.sleep(2)

    def check_computer_hit_the_target(shot, list_comp_hit_target_medium):
        """
        a function that checks if the computer got into the user's tank
        """
        print('Checking if the computer hit the target\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_comp_hit_target_medium:
            print('Damn! He knocked out your tank\n')
            list_comp_hit_target_medium.remove(shot[index])
            time.sleep(2)
        else:
            print('Ha-ha! Computer missed\n')
            time.sleep(2)

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
        game = True
        time.sleep(2)
        print("""Just a second...
        I will briefly talk about the rules of the game and begin\n""")
        time.sleep(3)
        print('The player and the computer take turns shooting at enemy tanks')
        time.sleep(3)
        print(f"""Enter a new number each time between
        1 and {len(computer_possible_tanks_list)}""")
        time.sleep(3)
        print("""If there is an enemy tank in the number
        entered by the user or selected by the computer,
        it is hit""")
        time.sleep(3)
        print("""The winner is the one who quickly knocks
        out all the enemy tanks\n""")
        time.sleep(3)
        print('And now let\'s start...\n')
        time.sleep(2)

        if moveChoice == 'user':
            while game:
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
        else:
            while game:
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
        print()
        print('Game Over')
        time.sleep(2)

    game_cycle(first_move)


def hard_game_level():
    """
    a function that displays the gameplay with easy difficulty
    """
    def user_tanks_choice():
        while True:
            time.sleep(1)
            print("Enter four numbers from 1 to 30 separated by a comma")
            time.sleep(1)
            print("These will be your tanks")
            time.sleep(1)
            print("Example: 3,10,14,25\n")

            user_tanks = input("Enter your data here:\n")

            time.sleep(1)

            user_tanks = user_tanks.split(",")

            # condition on the validity of the input data
            if validate_tanks_data(user_tanks):
                print(f"""Yours tanks are:
                {user_tanks[0]}
                {user_tanks[1]}
                {user_tanks[2]}
                {user_tanks[3]}\n""")
                break

        return user_tanks

    def validate_tanks_data(values):
        """
        checks the data entered by the user for compliance
        with the required ones and "catches" errors
        """
        try:
            [int(value) for value in values]
            if len(values) != 4:
                raise ValueError(
                    f"Exactly 3 values required, you provided {len(values)}"
                )
            if (
                int(values[0]) > 30 or int(values[0]) <= 0
                ) or (
                    int(values[1]) > 30 or int(values[1]) <= 0
                    ) or (
                        int(values[2]) > 30 or int(values[2]) <= 0
                        ) or (
                            int(values[3]) > 30 or int(values[3]) <= 0
                            ):
                raise ValueError("""The entered numbers must not be more
                than 10 and less than 1""")
            if (
                values[0] == values[1] or
                values[0] == values[2] or
                values[0] == values[3] or
                values[1] == values[2] or
                values[1] == values[3] or
                values[2] == values[3]
               ):
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
    computer_possible_tanks_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
        '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
        '22', '23', '24', '25', '26', '27', '28', '29', '30']

    # computer tanks
    computer_tanks = []

    def computer_tanks_choice(list_comp_tanks_hard):
        """
        A function that determines the computer's tanks
        by choosing a random number from a given list
        """
        time.sleep(2)
        print('And now the computer makes its choice... wait a second')
        time.sleep(2)
        print('The computer has 5 tank')
        time.sleep(2)
        computer_tanks_list = []
        while len(computer_tanks_list) != 5:
            for i in list_comp_tanks_hard:
                if i in computer_tanks_list:
                    continue
                else:
                    i = random.randint(1, len(list_comp_tanks_hard) - 1)
                    computer_tanks_list.append(str(i))
                    time.sleep(1)
                    break
        print('The computer has made its choice\n')
        return computer_tanks_list

    computer_tanks = (
        computer_tanks_choice(computer_possible_tanks_list)
        ).copy()

    # user maded moves
    user_maded_moves = []
    # user_possible_moves
    user_possible_moves = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
        ]
    # computer moves
    computer_moves = []

    def user_move(maded_moves, possible_moves):
        """The function describes the process of firing a shot,
        validates the data entered by the user,
        adds the user's move to the variable
        and removes the values entered by the user from the possible moves"""
        print()
        print('User turn')
        print(f'Your attempts: {maded_moves}')
        print(f'Possible moves: {possible_moves}')
        print(f'Your tanks: {user_tanks_choice}')
        print('Where do you order to shoot sir/ma\'am?')
        while True:
            user_shot = input('Enter a number from 1 to 30\n')
            print()

            if validate_user_shot(user_shot):
                print('Fire!\n')
                maded_moves.append(user_shot)
                possible_moves.remove(int(user_shot))
                time.sleep(2)
                break

    def validate_user_shot(value):
        """
        the function validates the data entered by the user
        and handles possible errors
        """
        try:
            if int(value) > 30:
                raise ValueError(
                    "The entered number must not be more than 30"
                )
            if int(value) < 1:
                raise ValueError(
                    "The entered number must not be less than 1"
                )
            if value in user_maded_moves:
                raise ValueError(
                    "You have already entered this value. Choose another"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True

    def shuffle_computer_move(list_shuf_comp_mov_hard):
        """
        A function that generates a list of random possible computer moves
        """
        random.shuffle(list_shuf_comp_mov_hard)
        shuffle = []
        for i in list_shuf_comp_mov_hard:
            shuffle.append(i)

        return shuffle

    def computer_move(list_comp_mov_hard):
        """
        A function that plays a computer shot and
        writes its shot to the corresponding variable
        """
        print()
        time.sleep(1)
        print('Computer turn')
        time.sleep(2)
        print('He shoots straight...')

        for value in list_comp_mov_hard:
            if value in computer_moves:
                continue
            else:
                print(value)
                computer_moves.append(str(value))
                time.sleep(2)
                break

    # computer shuffle move
    shuffle_computer_move = shuffle_computer_move(computer_possible_tanks_list)

    def check_user_hit_the_target(shot, list_user_hit_target_hard):
        """
        a function that checks if the user is in the tank
        """
        print('Checking if you hit the tank\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_user_hit_target_hard:
            print('Exactly! You knocked out an enemy tank\n')
            list_user_hit_target_hard.remove(shot[index])
            time.sleep(2)
        else:
            print('Miss ): Maybe you should aim better next time?\n')
            time.sleep(2)

    def check_computer_hit_the_target(shot, list_comp_hit_target_hard):
        """
        a function that checks if the computer got into the user's tank
        """
        print('Checking if the computer hit the target\n')
        time.sleep(2)
        index = len(shot) - 1
        if shot[index] in list_comp_hit_target_hard:
            print('Damn! He knocked out your tank\n')
            list_comp_hit_target_hard.remove(shot[index])
            time.sleep(2)
        else:
            print('Ha-ha! Computer missed\n')
            time.sleep(2)

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
        game = True
        time.sleep(2)
        print("""Just a second...
        I will briefly talk about the rules of the game and begin\n""")
        time.sleep(3)
        print(
            'The player and the computer take turns shooting at enemy tanks'
            )
        time.sleep(3)
        print(f"""Enter a new number each time between
        1 and {len(computer_possible_tanks_list)}""")
        time.sleep(3)
        print("""If there is an enemy tank in the number
        entered by the user or selected by the computer,
        it is hit""")
        time.sleep(3)
        print("""The winner is the one who quickly knocks out
        all the enemy tanks\n""")
        time.sleep(3)
        print('And now let\'s start...\n')
        time.sleep(2)

        if moveChoice == 'user':
            while game:
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
        else:
            while game:
                computer_move(shuffle_computer_move)
                check_computer_hit_the_target(
                    computer_moves, user_tanks_choice
                    )
                if len(user_tanks_choice) == 0:
                    print('Alas .. This time you lost ...')
                    game = False
                    break
                user_move(user_maded_moves, user_possible_moves)
                check_user_hit_the_target(user_maded_moves, computer_tanks)
                if len(computer_tanks) == 0:
                    print('Fantastic! You won!!!!')
                    game = False
                    break
        print()
        print('Game Over')
        time.sleep(2)

    game_cycle(first_move)


def game_start(difficulty):
    """
    a function that, based on processing the user's choice,
    launches the game in the appropriate difficulty
    """
    if difficulty == 'easy':
        easy_game_level()
    elif difficulty == 'medium':
        medium_game_level()
    else:
        hard_game_level()


def repeat_game():
    """
    A function that asks the user if he wants to play again
    """
    print("Do you want to play more? yes = 1; no = 2\n")
    will_repeat = input()

    while will_repeat != '1' and will_repeat != '2':
        print("""Incorrect data entered. Do you want to play more?
        yes = 1; no = 2\n""")
        will_repeat = input()

    if will_repeat == "1":
        user_choice = game_difficulty_selection()
        pick_user_level_game = check_difficulty(user_choice)
        main(pick_user_level_game)
    else:
        return


def main(pick_user_level_game):
    """
    the main function that launches the game process
    """
    game_start(pick_user_level_game)
    repeat_game()


# call main to start the game
main(pick_user_level_game)
