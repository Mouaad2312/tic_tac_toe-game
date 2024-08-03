# lets do another test for the x,o game
'''
how will our program work:
first we will need to print the board
then we will need to take turns between the computer and the user. the computer will make random moves. No logic behind them.
Basically there will be a loop that takes the computer choice then the user
then we will loop until the list doesnt have any '-'. then we will see who won
then we will print a congratulations message to the winner
we will try to make funtions so we can skip repetitiveness
'''
# import the random module that we will work with
import random


# the functions that we can apply. We will just try to recall them here
def board():
    for ele in game_board:
        print('  '.join(ele))
        print('-------')
    print()


def placement_check(choice, symbol):
    if choice == '1':
        game_board[0][0] = symbol
        board()
    elif choice == '2':
        game_board[0][1] = symbol
        board()
    elif choice == '3':
        game_board[0][2] = symbol
        board()
    elif choice == '4':
        game_board[1][0] = symbol
        board()
    elif choice == '5':
        game_board[1][1] = symbol
        board()
    elif choice == '6':
        game_board[1][2] = symbol
        board()
    elif choice == '7':
        game_board[2][0] = symbol
        board()
    elif choice == '8':
        game_board[2][1] = symbol
        board()
    elif choice == '9':
        game_board[2][2] = symbol
        board()


def check_winner(game_board, user_symbol, computer_symbol):
    for ele in game_board:
        if (ele == ['x', 'x', 'x'] and user_symbol == 'x') or (ele == ['o', 'o', 'o'] and user_symbol == 'o'):
            print('Congaratulations, you Won!!')
            return True
        elif (ele == ['x', 'x', 'x'] and computer_symbol == 'x') or (ele == ['o', 'o', 'o'] and computer_symbol == 'o'):
            print('You lost. See you next time')
            return True
        else:
            return False
    for j in range(3):
        if game_board[0][j] == game_board[1][j] == game_board[2][j] and game_board[0][j] == user_symbol:
            print('Concratulations, you Won!!')
            return True
        elif game_board[0][j] == game_board[1][j] == game_board[2][j] and game_board[0][j] == computer_symbol:
            print('You lost, see you next time')
            return True
        else:
            return False
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] or game_board[0][2] == game_board[1][1] ==
        game_board[2][0]) and game_board[1][1] == user_symbol:
        print('Congratulations, you Won!!')
        return True
    elif (game_board[0][0] == game_board[1][1] == game_board[2][2] or game_board[0][2] == game_board[1][1] ==
          game_board[2][0]) and game_board[1][1] == computer_symbol:
        print('You lost. See you next time')
        return True
    else:
        return False


# we will print a bunch of welcoming messages and the game rules

print('Welcome to the tic_tac_toe game. Lets start')
print("""
Tic-Tac-Toe Rules:

1. The board is a 3x3 grid with numbered positions:
   1  2  3
   -------
   4  5  6
   -------
   7  8  9

2. Players take turns to place their symbol (X or O) in an empty cell.

3. To make a move, enter the number of the cell where you want to place your symbol.

4. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.

5. If all cells are filled and no one has won, the game is a draw.

Have fun!
""")

# lets create our list and print it
game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
board()

# lets start looping
taken_placement = []
while True:
    user_symbol = input("What do you want to play with 'x' or'o': ")
    if user_symbol not in ['x', 'o']:
        print(" you get to choose from just two options. Either 'x' or 'o'")
    else:
        computer_symbol = 'o' if user_symbol == 'x' else 'x'

    while '-' in game_board:
        user_choice = input('Where do you wanna put your symbol in the game_board: ')
        taken_placement.append(user_choice)
        if user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("We already cited how placements are inputed. Please refer to the instructions")
            continue
        elif user_choice in taken_placement:
            print('This placement is already full. choose a free placement.')
            continue
        placement_check(user_choice, user_symbol)
        check_winner(game_board, user_symbol, computer_symbol)
        value_win = check_winner(game_board, user_symbol, computer_symbol)
        if value_win == True:
            break
        else:
            pass
        while True:
            computer_choice = str(random.randint(1, 9))
            if computer_choice in taken_placement:
                continue
            else:
                taken_placement.append(computer_choice)
                break
        placement_check(computer_choice, computer_symbol)
        check_winner(game_board, user_symbol, computer_symbol)
        value_win = check_winner(game_board, user_symbol, computer_symbol)
        if value_win == True:
            break
        else:
            pass

    game_status = input("Do you want to continue playing. Answer with a 'y' or 'n': ")
    if game_status not in ('y', 'n'):
        print('Your input was wrong. So we will exit the game.')
        break
    elif game_status == 'n':
        print('You have chosen to exit the game. It was nice to play with you. See you next time ')
        break
    else:
        print('OK! Lets go for another Tic-Tac-Toe game.')
        continue
