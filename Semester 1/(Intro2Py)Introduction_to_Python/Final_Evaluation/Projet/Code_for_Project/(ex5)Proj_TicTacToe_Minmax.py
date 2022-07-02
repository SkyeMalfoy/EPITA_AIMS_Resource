#!/usr/bin/env python3
"""
@Time  : 2022/5/26  11:20AM
@Author: Skye
@File  : Proj_TicTacToe_Minimax.py
"""

from math import inf as infinity
from random import choice
import platform
import time
from os import system


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell is None:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= len(board) ** 2),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = None
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def display(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        None: ' '
    }
    label = 1
    str_line = '--------'
    print('\n')
    for _ in range(len(state)):
        print(str_line, end="")
    print('-')
    # print(state)
    for _ in range(len(state)):
        print('*' + '-' * 7, end="")
    print("*")
    for row in range(len(state)):
        for column in range(len(state[row])):
            symbol = chars[state[row][column]]
            if label <= 9:
                if state[row][column] == None:
                    print('|' + ' ' * 3 + str(label) + ' ' * 3, end="")
                else:
                    print('|' + ' ' * 3 + symbol + ' ' * 3, end="")
            else:
                if state[row][column] == None:
                    print('|' + ' ' * 2 + str(label) + ' ' * 2, end="")
                else:
                    print('|' + ' ' * 2 + symbol + ' ' * 2, end="")
            label = int(label) + 1
        print("|")
        for _ in range(len(state)):
            print('*' + '-' * 7, end="")
        print("*")


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < board * board,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    print(depth)
    if depth == 0 or game_over(board):
        return

    print(f'Computer turn [{c_choice}]')
    display(board, c_choice, h_choice)

    if depth == len(board) ** 2:
        x_choice, y_choice = [], []
        for i in range(len(board)):
            x_choice.append(i)
            y_choice.append(i)
        x = choice(x_choice)
        y = choice(x_choice)
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = dict()
    print(len(board))
    key_input = 1
    for row in range(len(board)):
        for column in range(len(board)):
            moves[key_input] = [row, column]
            key_input += 1
    print(moves)

    # moves = {
    #     1: [0, 0], 2: [0, 1], 3: [0, 2],
    #     4: [1, 0], 5: [1, 1], 6: [1, 2],
    #     7: [2, 0], 8: [2, 1], 9: [2, 2],
    # }

    print(f'Human turn [{h_choice}]')
    display(board, c_choice, h_choice)

    while move < 1 or move > 16:
        try:
            move = int(input('Please input the number you want to put:'))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('This place is been taken, choose another place!')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('End!')
            exit()
        except (KeyError, ValueError):
            print('Choose wrongly, please give out another choose!')


def main():
    """
    Main function that calls all functions
    """
    h_choice = ''  # X or O, computer's choice will be given as the opposite.
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Player, choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('End!')
            exit()
        except (KeyError, ValueError):
            print('Choose wrongly, please give out another choose!')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    while first != 'Y' and first != 'N':
        try:
            first = input('Player wants to first to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('End!')
            exit()
        except (KeyError, ValueError):
            print('Choose wrongly, please give out another choose!')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        print(f'Human turn [{h_choice}]')
        display(board, c_choice, h_choice)
        print('Player Wins!')
    elif wins(board, COMP):
        print(f'Computer turn [{c_choice}]')
        display(board, c_choice, h_choice)
        print('Computer Wins!')
    else:
        display(board, c_choice, h_choice)
        print('Draw!')

    exit()


if __name__ == '__main__':
    HUMAN = -1
    COMP = +1
    size = int(input('Please input the size of the board:'))
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(None)
        board.append(row)
    main()
