#!/usr/bin/env python

NUM_ROWS = NUM_COL = 8


class Checkers(object):
    '''A checkers program'''

    def __init__(self):
        self.board = []

    def run(self):
        print 'run'
        self._createBoard()
        self.showBoard()

    def _createBoard(self):
        for x in range(NUM_ROWS):
            row = []
            for cell in range(NUM_COL):
                row.append('x')
            self.board.append(row)

    def showBoard(self):
        print self.board


if __name__ == '__main__':
    Checkers().run()
