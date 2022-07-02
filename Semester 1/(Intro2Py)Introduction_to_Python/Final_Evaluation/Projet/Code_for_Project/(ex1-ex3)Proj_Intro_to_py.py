#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/4/28  10:05AM
@Author: Skye
@File  : Proj_Intro_to_py.py
"""
import random
from itertools import combinations

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
        self.turn = 'b' #the white player's turn
        self.winner = None # remains until the end of the game, 'w' refers the winner is white, 'b' refers black, 'd' refers draw


    def allowedMoves(self):
        '''
        :return: a set of moves allowed to the current player from this state.
        '''
        allow_moves = set()
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] is None:
                    allow_moves.add((row, column))
        return allow_moves

    def applyMove(self, move):
        '''
        :param move: type of moves. 1.("place", square, piece) 2.("move", square1, square2)
        :return: the state that is obtained by applying "move" to the current state.(None is failure)
        '''
        action = move[0]
        allow_moves = self.allowedMoves()
        self.allow_moves = allow_moves

        #Judge which type of state it is.
        if action == "place": #When it's in "place" state.
            if move[1] in allow_moves:
                self.board[move[1][0]][move[1][1]] = move[2]
                place_result = True #To check if it is successful to place.
            else:
                place_result = False

        elif action == "move":
            square1 = move[1]
            square2 = move[2]
            if square1 not in allow_moves and square2 in allow_moves:
                self.board[square1[0]][square1[1]], self.board[square2[0]][square2[1]] = self.board[square2[0]][square2[1]], self.board[square1[0]][square1[1]]

        if self.turn == "w":
            self.turn = "b"
        elif self.turn == 'b':
            self.turn = "w"

        return self.board, self.turn, place_result

    def display(self):
        '''
        :return: the current state(board + whose turn)
        '''
        for row in range(len(self.board)):
            print('*' + '-' * 7, end="")
        print("*")
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == None:
                    print('|' + ' ' * 3 + " " + ' ' * 3, end="")
                else:
                    print('|' + ' ' * 3 + self.board[row][column] + ' ' * 3, end="")

            print("|")
            for _ in range(len(self.board)):
                print('*' + '-' * 7, end="")
            print("*")
        return self.board

    def clone(self):
        '''
        :return: a copy of the state
        '''
        clone_board = self
        return clone_board

    def __eq__(self, clone_board):
        '''
        :param other:
        :return: a boolean(where two states are the same)
        '''
        return (clone_board.board == self.board and clone_board.turn == self.turn)

class TicTacToeState(State):
    def __init__(self, size=3):
        super().__init__()
        self.SIZE = size
        self.board = list()
        for i in range(self.SIZE):
            row = list()
            for j in range(self.SIZE):
                row.append(None)
            self.board.append(row)

    #Rule of the game:
    def wins(self, bPlayer, wPlayer):
        win_conditions = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(2, 0), (1, 1), (0, 2)},
    ]
        if len(bPlayer) < 3:
            return None
        else:
            #Make all the possibilities of grouping method of black pieces
            bPlayer_pos = list(combinations(bPlayer, 3))
            for item in bPlayer_pos:
                if set(item) in win_conditions:
                    result = 'b_win'
                    return result
                else:
                    continue

        if len(wPlayer) < 3:
            return None
        else:
            wPlayer_pos = list(combinations(wPlayer, 3))
            for item in wPlayer_pos:
                if set(item) in win_conditions:
                    result = 'w_win'
                    return result
                else:
                    continue

class Player:
    def __init__(self, color):
        self.color = color # "w" or "b"

    def play(self, state):
        """
        :param state: the board and whose turn it is.
        :return: returns the move played in state 'state'
        """
        return random.choice(list(state.allowedMoves()))

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def play(self, turn, bPlayer, wPlayer):
        square_place = int(input("Please input the square to place the piece:"))
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        [square_row, square_col] = moves[square_place]

        if turn == 'b':
            bPlayer.append((square_row, square_col))
        else:
            wPlayer.append((square_row, square_col))
        # square_row = int(input("Please input the row to place:"))
        # square_col = int(input("Please input the row to place:"))
        print('You have place a piece on row:{0} column{1}!'.format(square_row + 1, square_col + 1))
        return square_row, square_col, bPlayer, wPlayer

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

#Ex2 test

# test2 = State()
# test2_child = TicTacToeState()
# print(test2_child.display())
# test2_child.applyMove(("place", (1, 1), "X"))
# test2.applyMove(('move', (1, 1), (2, 1)))
# print(test2_child.__eq__(test2_child.clone()))
# print(test2_child.allowedMoves())

#Ex3 test
def playGame(initialState):
    print("\'X\' represents \'Black\', \'O\' represents \'White\'")
    initialState.display()
    test3_player_child = HumanPlayer(initialState.turn)
    turn = initialState.turn
    w_record = []
    b_record = []
    while True:
        state = initialState
        print('It is {}\'s turn!'.format(turn))
        square_row, square_col,  b_record, w_record = test3_player_child.play(turn, b_record, w_record)
        if turn == 'w':
            piece = 'O'
        else:
            piece = 'X'
        board, turn, place_result = state.applyMove(('place', (square_row, square_col), piece))
        if place_result is False:
            print('Being taken, please place in another place')
            board, turn, place_result = state.applyMove(('place', (square_row, square_col), piece))
        state.board = board
        state.display()
        result = state.wins(b_record, w_record)
        #Game rules:
        if result == 'b_win':
            print('Black wins!')
            break

        elif result == 'w_win':
            print('White wins!')
            break

        #Board is full of pieces
        if len(state.allow_moves) == 1:
            print('Draw!')
            break

state = TicTacToeState()
playGame(state)