# this file serves as a Grid matrix All the operations will performed here
# Addtionally this file written in object oriented style with classes

import random

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        pairs = [i for i in range(self.size*self.size//2)] * 2
        random.shuffle(pairs)
        grid = [pairs[i*self.size:(i+1)*self.size] for i in range(self.size)]
        self.hidden = [[True]*self.size for _ in range(self.size)] # logic for hiding the element
        return grid

    def hide(self, row, col):
        self.hidden[row][col] = True

    def reveal(self, row, col):
        self.hidden[row][col] = False

    def is_revealed(self, row, col):
        return not self.hidden[row][col]

    def get_value(self, row, col):
        return self.grid[row][col]

    def is_all_covered(self):
        return not all(not cover for row in self.cover for cover in row)

    def is_all_revealed(self):
        return all(not hidden for row in self.hidden for hidden in row)
