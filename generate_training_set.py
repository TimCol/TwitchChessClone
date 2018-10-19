#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import chess.pgn
import numpy as np
from state import State
import csv


def read_csv(game=None):
    with open('Data/stockfish.csv', newline='') as csvfile:
        stockfishd = csv.DictReader(csvfile)
        n = 0
        for game in stockfishd:
            n += 1
            if n > 20: 
                break
            print(game['Event'])
            i = 0
            for score in game['MoveScores'].split(" "):
                i += 1 
                print("Game move %d, score is %d" % (i, int(score)))








def get_dataset(num_samples=None):
    X,Y = [], []
    gn = 0 
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    # pgn files in the Data folder
    for fn in os.listdir("Data"):
        pgn = open(os.path.join("Data", fn))
        while 1:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            res = game.headers['Result']
            if res not in values:
                    print("%s not in values" & (res))
                    continue
            value = values[res]
            board = game.board()
            for move in game.main_line():
                board.push(move)
                ser = State(board).serialize()
                X.append(ser)
                Y.append(value)
            print("parsing game number %d, got %d examples" % (gn, len(X)))
            if num_samples is not None and len(X) > num_samples:
                return X, Y
            gn += 1
        return X, Y

if __name__ == "__main__":
    # X,Y = get_dataset(1000)
    # np.savez("processed/dataset_25M.npz", X, Y)
    read_csv(game=5)
