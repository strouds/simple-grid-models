# simple-grid-models
A couple simple grid-based models (percolation and diffusion) I built to practice coding. Inspired by the Model Thinking 
course on Coursera by Scott Page, and the implementations of similar models on Netlogo. I tried to be organized in setting
up an Object Oriented approach, though I don't have any formal education on how to do this properly.

grid.py - contains a main Grid class that creates an empty grid and has methods for operating on it and visualizing it, and
a PorousGrid subclass that is a grid with a certain percentage of tiles randomly blocked off (as is commonly used in
percolation models)

diffusion.py - contains a Diffusion class that models a step-based diffusion process using a Grid instance

percolation.py - contains a Percolation class that models a step-based diffusion process using a Grid instance

run_diffusion.py - contains functions to initiate, run, visualize, and output a GIFs of Diffusion models

run_percolation.py - contains functions to initiate, run, visualize, and output GIFs of Percolation models

Various .gif files - sample outputs of the make_gif() functions in run_diffusion and run_percolation
  * some of the percolation samples run left to right, these are older files. The current code runs top to bottom.
