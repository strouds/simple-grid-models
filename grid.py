# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 07:50:50 2021

@author: phill
"""
import random, numpy
import matplotlib.pyplot as plt

class Grid(object):
    """ plain, empty grid """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.values = {}
        for i in range(width):
            for j in range(height):
                self.values[(i, j)] = 0
    
    def set_value(self, pos, value):
        """ updates grid dictionary value
            Key is pos in the format (x, y),
            Value is whatever values the model is using """
        self.values[pos] = value
    
    def update_values(self, values):
        """ replaces the whole dictionary of the Grid object """
        self.values = values
                
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_values(self):
        return self.values
    
    def get_value(self, pos):
        try:
            return self.values[pos]
        except:
            return None
    
    def get_neighborhood(self, pos):
        """ argument: pos is in the format (x, y)
            returns: list of the squares immediately adjacent
                to pos """
        x, y = pos
        neighborhood = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    if (x + i, y + j) in self.values:
                        # print(i, j)
                        neighborhood.append((x + i, y + j))
        return neighborhood
                
    def draw_grid(self, colorbar=False, save=False, filename=''):
        grid_values = numpy.zeros((self.height, self.width))
        for value in self.values:
            y, x = value # reversed bc imshow has weird axes
            grid_values[x][y] = self.values[value]
            # print(value, self.values[value])
        plt.imshow(grid_values)
        if colorbar:
            plt.colorbar()
        if save:
            plt.savefig(filename)
            plt.close()
        else:
            plt.show()

class PorousGrid(Grid):
    def __init__(self, width, height, P):
        super().__init__(width, height)
        for value in self.values:
            # makes boxes in the grid impenetrable with probability P
            if random.random() > P:
                self.values[value] = -1

####### DOES NTO WORK ######    
class Maze(Grid):
    def __init__(self, width, height):
        super().__init__(width, height)
        for value in self.values:
            self.values[value] = -1 # start with whole grid impenetrable
        while self.get_maze_ratio() < 0.6:
            start = random.choice(list(self.values.keys()))
            path, visited = self.generate_maze(start)
            for step in path:
                self.values[step] = 0
            print(self.get_maze_ratio())
        
    def generate_maze(self, start, path=[], visited=[]):
        path.append(start)
        visited.append(start)
        turns = self.get_turns(start, visited)
        if len(path) > 1:
            visits = self.mark_visited(path[-2], turns)
            for visit in visits:
                visited.append(visit)
        while len(turns) > 0:
            next_start = random.choice(turns)
            turns.remove(next_start)
            path, visited = self.generate_maze(next_start, path, visited)
            # update turns each loop so doesn't miss if a square was marked
            # visited in a recursive call
            turns = self.get_turns(start, visited)
        return path, visited
    
    def get_turns(self, pos, visited):
        x, y = pos
        turns = []
        for turn in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if turn in self.values and turn not in visited:
                turns.append(turn)
        return turns
    
    def mark_visited(self, last_step, turns):
        last_step_neighbors = self.get_neighborhood(last_step)
        visits = []
        for neighbor in last_step_neighbors:
            if neighbor not in turns:
                visits.append(neighbor)
        print(visits)
        return visits
    
    def get_maze_ratio(self):
        holes = 0
        for value in self.values:
            if self.values[value] == 0:
                holes += 1
        return holes/len(self.values)