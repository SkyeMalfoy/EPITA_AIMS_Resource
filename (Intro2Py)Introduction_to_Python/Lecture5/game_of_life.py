#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time  : 2022/5/3  下午2:37
@Author: Skye
@File  : game_of_life.py 
"""
import random
import time
import os

class GameOfLife:
    def __init__(self, height, width, ratio=0.3):
        """
        :param height: height of the grid
        :param width: width of the grid
        :param ratio: ratio of live cell
        """
        self.height = height
        self.width = width
        self.grid = list()
        for i in range(self.height):
            row = list()
            for j in range(self.width):
                row.append(random.random() < ratio)
            self.grid.append(row)
        self.ratio = ratio

    def printGrid(self):
        """
        Print the current grid on the screen
        :return: the grid
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] is True:
                    print("O", end=" ")
                else:
                    print(" ", end=" ")
            print("|")
        return self.grid


    def numberOfNeighbors(self, i, j):
        """
        count the number of live neighbors
        square = (i, j)
        :param i: the 0th param of square
        :param j: the 1st param of square
        :return:
        """
        nearby = []
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue
                else:
                    x = x % self.height
                    y = y % self.width
                    nearby.append(self.grid[x][y])
        # print(nearby)
        return len(list(filter(lambda x: x is True, nearby)))


    def nextGeneration(self):
        """
        compute the next generation of current grid
        :return: the next grid.
        """
        #go through the grid
        for i in range(self.height):
            for j in range(self.width):
                count = self.numberOfNeighbors(i, j)
                if self.grid[i][j] is True:
                    if count < 2 or count > 3:
                        self.grid[i][j] = False
                    else:
                        continue
                else:
                    if count == 3:
                        self.grid[i][j] = True
        # print(self.grid)
        return self.grid

    def animate(self, N=100, frame_time=0.1):
        """
        :param N: make N generations to anime
        :param frame_time: the time between each frame.
        :return:
        """
        for i in range(10):
            self.nextGeneration()
            self.printGrid()
            os.system('clear')
            time.sleep(frame_time)
            print("\n")

if __name__ == '__main__':
    test = GameOfLife(10, 10)
    print(test.animate())
    # test.printGrid()
    # print(test.numberOfNeighbors(0, 0))