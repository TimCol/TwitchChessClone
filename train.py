#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import chess.pgn
from state import State

# pgn files in the Data folder
for fn in os.listdir("Data"):
    pgn = open(os.path.join("Data", fn))
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
        except Exception:
            print("exception") 
            break
        value = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
        board = game.board()
        for move in game.main_line():
            board.push(move)
            print(value, State(board).serialize()) 
    break
