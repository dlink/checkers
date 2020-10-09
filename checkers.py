#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        i = 0
        for x in range(NUM_ROWS):
            i += 1
            row = []
            for cell in range(NUM_COL):
                if i in (1, 2):
                    row.append(u'◯')
                elif i in (7, 8):
                    row.append(u'✪')
                else:
                    row.append(u' ')
            self.board.append(row)

    def showBoard(self):
        board_str = u''
        board_str += u'┌───┬───┬───┬───┬───┬───┬───┬───┐\n'
        i = 0
        for row in self.board:
            i += 1
            for cell in row:
                board_str += u'│ %s ' % cell
            board_str += u'│\n'
            if i < NUM_ROWS:
                board_str += u'├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        board_str += u'└───┴───┴───┴───┴───┴───┴───┴───┘\n'
        print board_str

if __name__ == '__main__':
    Checkers().run()
