#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/28  上午10:05
@Author: Skye
@File  : board.py 
"""

class Board:
    def __init__(self, size):
        self.board = list()
        self.size = size
        for i in range(size):
            row = list()
            for j in range(size):
                row.append(None)
            self.board.append(row)

    def place(self, piece, square): #initialize the board square.
        """
        :param piece: string （the thing to put in the board)
        :param square: tuple (the indexes of piece to put)
        :return: True or False
        """
        (r, c) = square
        if self.board[r][c] == None:
            self.board[r][c] = piece
            return True
        else:
            return False

    def isEmpty(self, square): #check if the square is been occupied.
        """
        :param square: tuple (the indexes the judge if there is something)
        :return: True or Flase
        """
        (r, c) = square
        return (self.board[r][c] == None)

    def display(self):  #prints the board
        # for row in [self.size[i * 3: (i + 1) * 3] for i in range(3)]:
        #     # print(row)
        #     print('|' + '|'.join(row) + '|')
        return self.board

    def remove(self, square):
        (r, c) = square
        if self.board[r][c] != None:
            self.board[r][c] = None
            return True
        else:
            return False

    def move(self, square1, square2):
        (r1, c1) = square1
        (r2, c2) = square2
        if self.board[r1][c1] == None or self.board[r2][c2] != None:
            return False
        else:
            self.board[r2][c2] = self.board[r1][c1]
            self.board[r1][c1] = None
            return True


    def clone(self): #returns a copy of the board
        return self.board

    def __eq__(self, other): #check if the current board is the same as other.
        return self.board == other

class State:
    def __init__(self):
        self.board = None
        self.turn = 'w' #the white player's turn
        self.winner = None # remains until the end of the game, 'w' refers the winner is white, 'b' refers black, 'd' refers draw

    def


###Ex1 test
# test = Board(3)
# print(test.display())
# board = test.place("X", (1, 2))
# # print(test.display())
# print(test.display())
# # test.remove((1,2))
# # print(test.display())
# board = test.move((1, 2), (0, 2))
# print(test.display())
# board_clone = test.clone()
# print(test.__eq__(board_clone))

###Ex2 test
