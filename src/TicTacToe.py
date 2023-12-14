import random

#global variables
board = [' ' for x in range(10)]
player = 'X'
computer = 'O'
winner = None
turn = 'player'

#board
def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#check if board is full
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#check if there is a winner

def check_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

#player move
def player_move(board):
    global turn
    turn = 'player'
    move = input('Select a position to place an \'X\' (1-9): ')
    move = int(move)
    if board[move] == ' ':
        board[move] = player
    else:
        print('That space is already taken.\n')
        player_move(board)

#computer move

def computer_move(board):
    global turn
    turn = 'computer'
    #check for win
    for i in range(1,10):
        if board[i] == ' ':
            board[i] = computer
            if check_winner(board, computer):
                return
            else:
                board[i] = ' '
    #check for player win
    for i in range(1,10):
        if board[i] == ' ':
            board[i] = player
            if check_winner(board, player):
                board[i] = computer
                return
            else:
                board[i] = ' '
    #check for corners
    corners = []
    for i in [1,3,7,9]:
        if board[i] == ' ':
            corners.append(i)
    if len(corners) > 0:
        board[random.choice(corners)] = computer
        return
    #check for center
    if board[5] == ' ':
        board[5] = computer
        return
    #check for edges
    edges = []
    for i in [2,4,6,8]:
        if board[i] == ' ':
            edges.append(i)
    if len(edges) > 0:
        board[random.choice(edges)] = computer
        return

#main game loop

def main():
    global turn
    print('Welcome to Tic Tac Toe!')
    print_board(board)
    while not(is_board_full(board)):
        if not(check_winner(board, computer)):
            player_move(board)
            print_board(board)
        else:
            print('Computer wins!')
            break
        if not(check_winner(board, player)):
            computer_move(board)
            print_board(board)
        else:
            print('Player wins!')
            break
    if is_board_full(board):
        print('Tie game!')

#play again

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
