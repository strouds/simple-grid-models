# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:58:07 2021

@author: phill
"""
from grid import Grid, PorousGrid
from diffusion import Diffusion
import imageio, os

def setup_diff(width, height, diffusion_prob, grid_type, P):
    if grid_type == PorousGrid:
        grid = PorousGrid(width, height, P)
    else:
        grid = Grid(width, height, diffusion_prob)
    diff = Diffusion(grid, diffusion_prob)
    diff.start_position((width//2, height//2))
    return diff, grid

def step(diff, grid):
    diff.step()
    grid.draw_grid()

def run_diff(width, height, diffusion_prob, grid_type, P): 
    diff, grid = setup_diff(width, height, diffusion_prob, grid_type, P)
    grid.draw_grid()
    path = True
    while path == True:
        path = diff.step()
        # print(path)
        grid.draw_grid()

# run_diff(25, 25, .1, PorousGrid, .4)

def make_gif(width, height, diffusion_prob, grid_type, P, gif_name):
    diff, grid = setup_diff(width, height, diffusion_prob, grid_type, P)
    path = True
    counter = 0
    filenames = []
    grid.draw_grid(save=True, filename=str(counter)+'.png')
    filenames.append(str(counter)+'.png')
    counter += 1
    while path:
        path = diff.step()
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