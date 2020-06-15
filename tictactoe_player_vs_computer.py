#Tic Tac Toe w/ the Computer by Nishant S

import sys

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

#function for player move
def player_move():
    move = int(input('select a square from 1-9 '))
    pos = move - 1
    return pos

#function for computer move
def comp_moveO(board):
    while board:
        if board[4] == ' ':
            return 4
        elif board[4] != ' ':
            if board[1] == ' ':
                return 1
            

        #horizontal
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

        #Vertical
        
        elif board[0]=='X' and board[3]=='X':
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

        #diagonal
        elif board[0]=='X' and board[4]=='X':
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

        #anticipated tricks
        elif board[1]=='X' and board[3]=='X':
            return 0
        elif board[1]=='X' and board[5]=='X':
            return 2

        elif board[7]=='X' and board[3]=='X':
            return 6
        elif board[7]=='X' and board[5]=='X':
            return 8
        
        elif board[1] != ' ':
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


def comp_moveX(board):
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
        if board[0]=='O' and board[1]=='O':
            return 2
        elif board[1]=='O' and board[2]=='O':
            return 0
        elif board[0]=='O' and board[2]=='O':
            return 1
        
        elif board[3]=='O' and board[4]=='O':
            return 5
        elif board[4]=='O' and board[5]=='O':
            return 3
        elif board[3]=='O' and board[5]=='O':
            return 4

        elif board[6]=='O' and board[7]=='O':
            return 8
        elif board[7]=='O' and board[8]=='O':
            return 6
        elif board[6]=='O' and board[8]=='O':
            return 7

        #Vertical
        
        elif board[0]=='O' and board[3]=='O':
            return 6
        elif board[3]=='O' and board[6]=='O':
            return 0
        elif board[0]=='O' and board[6]=='O':
            return 3
        
        elif board[1]=='O' and board[4]=='O':
            return 7
        elif board[4]=='O' and board[7]=='O':
            return 1
        elif board[7]=='O' and board[1]=='O':
            return 4
        

        elif board[2]=='O' and board[5]=='O':
            return 8
        elif board[5]=='O' and board[8]=='O':
            return 2
        elif board[2]=='O' and board[8]=='O':
            return 5

        #diagonal
        elif board[0]=='O' and board[4]=='O':
            return 8
        elif board[4]=='O' and board[8]=='O':
            return 0
        elif board[0]=='O' and board[8]=='O':
            return 4

        elif board[2]=='O' and board[4]=='O':
            return 6
        elif board[4]=='O' and board[6]=='O':
            return 2
        elif board[2]=='O' and board[6]=='O':
            return 4

        #anticipated tricks
        elif board[1]=='O' and board[3]=='O':
            return 0
        elif board[1]=='O' and board[5]=='O':
            return 2

        elif board[7]=='O' and board[3]=='O':
            return 6
        elif board[7]=='O' and board[5]=='O':
            return 8
        
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


#function to kickoff the game
def kickoff(x,o):
    if x == 'computer':
        standing1('computer')
    elif x == 'player':
        standing('player')

#function to identify which squares of the board are occupied by whom
#if player picks 'X'
def standing(player):

    winner(board)

    if player == 'player':
        position = player_move()
        if board[position] == ' ':
            board[position] = 'X'
            board_display()
            standing('computer')

        elif board[position] != ' ':
            print('That square is already taken, try again!')
            standing(player)

    elif player == 'computer':

        c_position = comp_moveO(board)
        board[c_position] = 'O'
        print("Computer Move: ")
        board_display()
        winner(board)
        standing('player')


#function to identify which squares of the board are occupied by whom
#if player picks 'O'
def standing1(player):

    winner(board)

    if player == 'player':
        position = player_move()
        if board[position] == ' ':
            board[position] = 'O'
            board_display()
            standing1('computer')

        elif board[position] != ' ':
            print('That square is already taken, try again!')
            standing1(player)

    elif player == 'computer':

        c_position = comp_moveX(board)
        board[c_position] = 'X'
        print("Computer Move: ")
        board_display()
        winner(board)
        standing1('player')

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
    tile = input("Would you like to be 'X' or 'O'? ")
    if tile == 'X':
        first = 'player'
        second = 'computer'
        kickoff(first,second)
    elif tile == 'O':
        first = 'computer'
        second = 'player'
        kickoff(first,second)
    else:
        print("Invalid option, pick 'X' or 'O' ")

start()
