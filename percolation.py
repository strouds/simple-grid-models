# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:08:10 2021

@author: phill
"""

class Percolation(object):
    """ simple percolation model """
    def __init__(self, grid):
        """ grid is a PorousGrid instance """
        self.grid = grid
        for i in range(self.grid.get_width()):
            if self.grid.get_value((i, 0)) == 0:
                grid.set_value((i, 0), 1)
        self.working_layer = 0
    
    def step(self):
        next_layer = self.working_layer + 1
        path = False
        for i in range(self.grid.get_width()):
            # tests if each tile in the most recently worked layer
            #   has been filled or not
            if self.grid.get_value((i, self.working_layer)) == 1:
                # if it has, checks adjacent tiles on the next layer
                #   for empty spaces and fills them
                for j in [i - 1, i, i + 1]:
                    if self.grid.get_value((j, next_layer)) == 0:
                        self.grid.set_value((j, next_layer), 1)
                        path = True # at least one legal tile on the next 
                                    # layer has been filled
                        # print(j, next_layer)
        # lets the calling function know when to stop
        self.working_layer = next_layer
        return path

