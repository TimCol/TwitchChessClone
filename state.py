#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import chess

class State(object):
    def __init__(self):
        self.board = chess.Board()
    
    def serialize(self):
        # 257 bits according to readme
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        return 0

if __name__ == "__main__":
    s = State()
    print(s.edges())


