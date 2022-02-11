#!/usr/bin/env python

from board import Board

class Checkers(object):
    '''A checkers program'''

    def __init__(self):
        self.board = Board()

    def run(self):
        print 'run'
        self.board.show()

if __name__ == '__main__':
    Checkers().run()
