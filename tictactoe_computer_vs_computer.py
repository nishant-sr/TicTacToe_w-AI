import sys
import random

sys.setrecursionlimit(1500)

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def board_display():
    print("          ")
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print("          ")


#function to check horizontally
def horizontal(board):

    if board[0]=='X' and board[1]=='X':
        return 2
    elif board[1]=='X' and board[2]=='X':
        return 0
    elif board[0]=='X' and board[2]=='X':
        return 1

    elif board[3]=='X' and board[4]=='X':
        return 5
    elif board[4]=='X' and board[5]=='X':
        return 3
    elif board[3]=='X' and board[5]=='X':
        return 4

    elif board[6]=='X' and board[7]=='X':
        return 8
    elif board[7]=='X' and board[8]=='X':
        return 6
    elif board[6]=='X' and board[8]=='X':
        return 7
    
#function to check vertically
def vertical(board):

    if board[0]=='X' and board[3]=='X':
        return 6
    elif board[3]=='X' and board[6]=='X':
        return 0
    elif board[0]=='X' and board[6]=='X':
        return 3
        
    elif board[1]=='X' and board[4]=='X':
        return 7
    elif board[4]=='X' and board[7]=='X':
        return 1
    elif board[7]=='X' and board[1]=='X':
        return 4
        

    elif board[2]=='X' and board[5]=='X':
        return 8
    elif board[5]=='X' and board[8]=='X':
        return 2
    elif board[2]=='X' and board[8]=='X':
        return 5
    
#function to check diagonally
def diagonal(board):
    
    if board[0]=='X' and board[4]=='X':
        return 8
    elif board[4]=='X' and board[8]=='X':
        return 0
    elif board[0]=='X' and board[8]=='X':
        return 4

    elif board[2]=='X' and board[4]=='X':
        return 6
    elif board[4]=='X' and board[6]=='X':
        return 2
    elif board[2]=='X' and board[6]=='X':
        return 4

#function to check for tricks
def tricks(board):

    if board[1]=='X' and board[3]=='X':
        return 0
    elif board[1]=='X' and board[5]=='X':
        return 2

    elif board[7]=='X' and board[3]=='X':
        return 6
    elif board[7]=='X' and board[5]=='X':
        return 8

#function for computer move
def comp_move1(board):
    while board:
        if board[4] == ' ':
            return 4
        elif board[4] != ' ':
            if board[1] == ' ':
                return 1

        #horizontal
        horizontal(board)

        #Vertical
        vertical(board)

        #diagonal
        diagonal(board)

        #anticipated tricks
        tricks(board)

        if board[1] != ' ':
            if board[3] == ' ':
                return 3
            elif board[3] != ' ':
                if board[7] == ' ':
                    return 7
                elif board[7] != ' ':
                    if board[5] == ' ':
                        return 5
                    else:
                        if board[0] == ' ':
                            return 0
                        elif board[0] != ' ':
                            if board[2] == ' ':
                                return 2
                            elif board[2] != ' ':
                                if board[6] == ' ':
                                    return 6
                                elif board[6] != ' ':
                                    if board[8] == ' ':
                                        return 8

def comp_move(board):
    while board:
        if board[4] == ' ':
            return 4
        elif board[4] != ' ':
            if board[1] == ' ':
                return 1
            elif board[1] != ' ':
                if board[3] == ' ':
                    return 3

        #horizontal
        horizontal(board)

        #Vertical
        vertical(board)

        #diagonal
        diagonal(board)

        #anticipated tricks
        tricks(board)

        if board[3] != ' ':
            if board[7] == ' ':
                return 7
            elif board[7] != ' ':
                if board[5] == ' ':
                    return 5
                else:
                    if board[0] == ' ':
                        return 0
                    elif board[0] != ' ':
                        if board[2] == ' ':
                            return 2
                        elif board[2] != ' ':
                            if board[6] == ' ':
                                return 6
                            elif board[6] != ' ':
                                if board[8] == ' ':
                                    return 8



#function to identify which squares of the board are occupied by whom
#if player picks 'X'
def standing(player='computer1'):

    winner(board)

    if player == 'computer1':

        c_position = comp_move1(board)
        board[c_position] = 'X'
        board_display()
        standing('computer')


    elif player == 'computer':

        c_position = comp_move(board)
        board[c_position] = 'O'
        board_display()
        standing('computer1')


#function for finding out who won
#function needs to see the board to determine who won
def winner(b):

    if ' ' not in b:
        print("TIE")
        quit()

    elif \
    (b[0]=='X' and b[3]=='X' and b[6]=='X')or\
    (b[1]=='X' and b[4]=='X' and b[7]=='X')or\
    (b[2]=='X' and b[5]=='X' and b[8]=='X')or\
    (b[0]=='X' and b[1]=='X' and b[2]=='X')or\
    (b[3]=='X' and b[4]=='X' and b[5]=='X')or\
    (b[6]=='X' and b[7]=='X' and b[8]=='X')or\
    (b[0]=='X' and b[4]=='X' and b[8]=='X')or\
    (b[2]=='X' and b[4]=='X' and b[6]=='X'):
        print(" X WINS")
        quit()

    elif \
    (b[0]=='O' and b[3]=='O' and b[6]=='O')or\
    (b[1]=='O' and b[4]=='O' and b[7]=='O')or\
    (b[2]=='O' and b[5]=='O' and b[8]=='O')or\
    (b[0]=='O' and b[1]=='O' and b[2]=='O')or\
    (b[3]=='O' and b[4]=='O' and b[5]=='O')or\
    (b[6]=='O' and b[7]=='O' and b[8]=='O')or\
    (b[0]=='O' and b[4]=='O' and b[8]=='O')or\
    (b[2]=='O' and b[4]=='O' and b[6]=='O'):
        print(" O WINS")
        quit()

    else:
        pass

#function to start the game
def start():
    print("Welcome to TIC TAC TOE")
    standing('computer1')


start()
