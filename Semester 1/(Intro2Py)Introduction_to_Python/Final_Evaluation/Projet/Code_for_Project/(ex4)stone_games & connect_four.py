#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/5/29  上午9:38
@Author: Skye
@File  : stone_games & connect_four.py 
"""
# import random
#
# class Player:
#     def __init__(self, color):
#         self.color = color # "w" or "b"
#
#     def play(self, state):
#         """
#         :param state: the board and whose turn it is.
#         :return: returns the move played in state 'state'
#         """
#         return random.choice(list(state.allowedMoves()))
#
# class Stones():
#     def __init__(self, minStones=9, maxStones=25):
#         self.numStones = random.randint(minStones, maxStones)
#         self.turn = 'w'
#     def playGame(self, player1, player2):
#         print("There are {} stones in total!".format(self.numStones))
#         while self.numStones > 0:
#             print("Turn of: " + self.turn)
#             if self.turn == 'w':
#                 print("It's White player's turn!")
#                 self.numStones = self.numStones - player1.play()
#             else:
#                 print("It's Black player's turn!")
#                 self.numStones = self.numStones - player2.play()
#             if self.numStones <= 0:
#                 if self.turn == 'w':
#                     print("White player won!")
#                 else:
#                     print("Black player won!")
#             else:
#                 print("remaining Stones: ", self.numStones)
#             if self.turn == 'w':
#                 self.turn = 'b'
#             else:
#                 self.turn = 'w'
#
#
# class HumanStonesPlayer(Player):
#     def __init__(self, color):
#         super().__init__(color)
#
#     def play(self):
#         stones = int(input("Please input the num of stones you wanna pick:(1-3)\n"))
#         if stones < 1 or stones > 3:
#             print('Wrong input, please input the number again!')
#             return self.play()
#         return stones
#
# #Running the game:
# stonesGame = Stones()
# player1 = HumanStonesPlayer('w')
# player2 = HumanStonesPlayer('b')
# stonesGame.playGame(player1, player2)



#---------------Connectfour Game---------------
import random

class Player:
    def __init__(self, color):
        self.color = color # "w" or "b"

    def play(self, state):
        """
        :param state: the board and whose turn it is.
        :return: returns the move played in state 'state'
        """
        return random.choice(list(state.allowedMoves()))

class State:
    def __init__(self, board, turn, winner):
        self.board = board
        self.turn = turn #the white player's turn
        self.winner = winner # remains until the end of the game, 'w' refers the winner is white, 'b' refers black, 'd' refers draw


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

class ConnectFourState(State):
    def __init__(self, board=Board(4), turn='w', winner=None):
        super().__init__(board, turn, winner)

    def allowedMoves(self):
        size = self.board.size
        connectFourBoard = self.board.board
        moves = []
        for i in range(size):
            if (connectFourBoard[0][i] == None):
                moves.append(i)
        return moves

    def checkIfWinner(self, square, color):
        size = self.board.size
        connectFourBoard = self.board.board
        sum = 0

        # Check Horizental
        for i in range(size):
            if (connectFourBoard[square[0]][i] == color):
                sum = sum + 1

        # Check if someone won
        if sum == size:
            return True
        sum = 0

        # Check Vertical
        for i in range(size):
            if (connectFourBoard[i][square[1]] == color):
                sum = sum + 1
                # Check if someone won
        if sum == size:
            return True
        sum = 0

        # check diagonal (up right, down left)
        for i in range(size):
            if (i + square[0] < size and i + square[1] < size):
                if connectFourBoard[square[0] + i][square[1] + i] == color:
                    sum = sum + 1

        for i in range(1, size):
            if (square[0] - i >= 0 and square[1] - i >= 0):
                if connectFourBoard[square[0] - i][square[1] - i] == color:
                    sum = sum + 1

        if sum >= size:
            return True
        sum = 0

        # check diagonal (down right, up left)
        for i in range(size):
            if (square[0] - i >= 0 and i + square[1] < size):
                if connectFourBoard[square[0] - i][i + square[1]] == color:
                    sum = sum + 1

        for i in range(1, size):
            if (square[0] + i < size and square[1] - i >= 0):
                if connectFourBoard[square[0] + i][square[1] - i] == color:
                    sum = sum + 1

        # Check if someone won
        if sum >= size:
            return True
        sum = 0

        return False

    def playGame(self, white, black):
        size = self.board.size
        connectFourBoard = self.board.board
        self.display()
        print("playable moves ", end='')
        print(self.allowedMoves())
        if len(self.allowedMoves()) == 0:
            print("Draw, Game Over!")
        while self.winner == None:
            print('Turn of: ' + self.turn)
            move = None
            squareToMove = -1
            if self.turn == 'w':
                squareToMove = white.play()
            else:
                squareToMove = black.play()
            if squareToMove in self.allowedMoves():
                highestTile = 0
                for i in (range(size)):
                    if connectFourBoard[size - i - 1][squareToMove] == None:
                        highestTile = size - i - 1
                        print(highestTile)
                        break
                self.applyMove(('place', (highestTile, squareToMove), self.turn))
                self.display()
                someoneOne = self.checkIfWinner([highestTile, squareToMove], self.turn)
                print(someoneOne)
                if someoneOne:
                    print(self.turn + ' won!')
                    return
                if self.turn == 'w':
                    self.turn = 'b'
                else:
                    self.turn = 'w'

class HumanConnectFourPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def play(self):
        correctUserInput = True
        return int(input("Enter a column to place your color: "))

## To run the game type this code
player1 = HumanConnectFourPlayer('w')
player2 = HumanConnectFourPlayer('b')
connectFourGame = ConnectFourState()
connectFourGame.display()
connectFourGame.playGame(player1, player2)