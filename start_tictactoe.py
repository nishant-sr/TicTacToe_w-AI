#TIC-TAC-TOE by Nishant S.

import tictactoe_player_vs_computer.py
import tictactoe_computer_vs_computer.py

def start():
    option = input("Welcome, if you would like to play the computer, press '1', if you would like the computer to play itself, pres '2' ")
    if option == '1':
        exec(open('tictactoe_player_vs_computer.py').read())
    else:
        exec(open('tictactoe_computer_vs_computer.py').read())


start()
