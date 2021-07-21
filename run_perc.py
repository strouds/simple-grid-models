# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:02:22 2021

@author: phill
"""

from grid import PorousGrid
from percolation import Percolation
import imageio, os

def setup_perc(width, height, P):
    grid = PorousGrid(width, height, P)
    perc = Percolation(grid)
    return grid, perc

def step(grid, perc):
    perc.step()
    grid.draw_grid()
    
def run(width, height, P):
    grid, perc = setup_perc(width, height, P)
    path = True
    while path:
        path = perc.step()
        grid.draw_grid()

# run(25, 50, .55)

def make_gif(width, height, P, gif_name):
    grid, perc = setup_perc(width, height, P)
    path = True
    counter = 0
    filenames = []
    grid.draw_grid(save=True, filename=str(counter)+'.png')
    filenames.append(str(counter)+'.png')
    counter += 1
    while path:
        path = perc.step()
        grid.draw_grid(save=True, filename=str(counter)+'.png')
        filenames.append(str(counter)+'.png')
        counter += 1
    # build gif
    with imageio.get_writer(gif_name, mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
    # Remove files
    for filename in set(filenames):
        os.remove(filename)