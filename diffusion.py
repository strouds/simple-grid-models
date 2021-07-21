# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:29:29 2021

@author: phill
"""
import random

class Diffusion(object):
    def __init__(self, grid, diffusion_prob):
        self.grid = grid
        self.diffusion_prob = diffusion_prob
    
    def start_position(self, pos):
        self.grid.set_value(pos, 1)
    
    def step(self):
        working_values = self.grid.get_values().copy()
        path = False # tracks if no more legal moves
        for pos in self.grid.get_values():
            if self.grid.get_value(pos) == 0:
                neighborhood = self.grid.get_neighborhood(pos)
                prob = 0
                for neighbor in neighborhood:
                    if self.grid.get_value(neighbor) == 1:
                        prob += 1
                        path = True # if this conditional is reached, there is
                                    # at least one legal square to move to
                # print(prob)
                working_values[pos] = random.random() < prob * self.diffusion_prob
        self.grid.update_values(working_values)
        return path
        
