from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''
    # Keep asking player 1 to use mark X | O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O:').upper()
    # Assign player 2, the remain marker
    player1 = marker
    if player1 == 'X':
        player2 = '0'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (board[1] == board[2] == board[3] == marker) or \
      (board[4] == board[5] == board[6] == marker) or \
      (board[7] == board[8] == board[9] == marker) or \
      (board[1] == board[4] == board[7] == marker) or \
      (board[2] == board[5] == board[8] == marker) or \
      (board[3] == board[6] == board[9] == marker) or \
      (board[1] == board[5] == board[9] == marker) or \
      (board[3] == board[5] == board[7] == marker)

def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (0-9)'))
    return position

def replay():
    choice = input('Play again? Enter Y or N:')
    return choice == 'Y'

print('Welcome to Tic-tac-toe')

while True:
    # Set up (board, who first, choose marker)
    board = [''] * 10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input('Ready to play? Y/N:').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    # Game play
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(board)
            # Choose a position
            position = player_choice(board)
            # Place the marker on board
            place_marker(board, player1_mark, position)

            # Check if they won
            if win_check(board, player1_mark):
                display_board(board)
                print('Player 1 has won!!')
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Show the board
            display_board(board)
            # Choose a position
            position = player_choice(board)
            # Place the marker on board
            place_marker(board, player2_mark, position)

            # Check if they won
            if win_check(board, player2_mark):
                display_board(board)
                print('Player 2 has won!!')
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 1'