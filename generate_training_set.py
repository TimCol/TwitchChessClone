#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import chess.pgn
import numpy as np
from state import State
import csv

def read_csv():
    with open('Data/stockfish.csv', newline='') as csvfile:
        scores = {}
        stockfishd = csv.DictReader(csvfile)
        gameCounter = 1
        for game in stockfishd:
            moveScore = []
            for score in game['MoveScores'].split(" "):
                moveScore.append(score)
            scores[gameCounter] = moveScore
            gameCounter += 1
        return scores

def normalize(x):
    if x == "NA":
        return 2 
    elif int(x) >= 50:  
        return 1 
    elif int(x) <= -50:
        return -1
    elif -50 < int(x) < 50: 
        return 0 

def get_dataset(num_samples=None):
    X,Y = [], []
    gn = 1 
    pgn = open("Data/data.pgn")

    while 1:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        board = game.board()
        mn = 0
        for move in game.main_line():
            board.push(move)
            try:
                score = normalize(scores[gn][mn])
            except:
                print("Error with Game %d" % gn)
                pass
            Y.append(score)
            ser = State(board).serialize()
            X.append(ser)
            mn += 1
        print("parsing game number %d, got %d examples" % (gn, len(X)))
        if num_samples is not None and len(X) > num_samples:
            return X, Y
        gn += 1
    return X, Y

if __name__ == "__main__":
    scores = read_csv()
    X,Y = get_dataset(1000000)
    np.savez("processed/dataset.npz", X, Y)
