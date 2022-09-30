# Simulation-of-Conway-s-game-of-life
This project is an implementation of Conway’s game of life. This simulation consists of a grid. Each grid is referred to as a cell. The simulation moves forward in discrete time steps. At each time step a cell is marked as either alive or dead according to the following rules:
• If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
• If the cell is dead, then it springs to life only in the case that it has 3 live neighbors


Here I use python’s object oriented concept also vectorization.
A function which calls conway_assignment_two (Ass3_script1). This function contains a loop. Each iteration through this loop represents a single time-step of our simulation. This function takes a parameter which causes it to save the board state for each time-step and return this board state history as a list.
 Function conway_assignment_three (Ass3_script1)without loop here this script using convolve2d from scipy  and vectorize from numpy
Ass3_script2 which runs simulation for a number of board sizes (starting at 1000x1000) and
increasing in increments of 250x250 up to the largest size can simulate for 100 time steps.(In larger size will end up with memory error)
This script run both conway_assignment_two and conway_assignment_three functions.output a graph of the time steps per millisecond for each board size you attempt for both implementation(vectorized and loop method).
Ass3_script4 that runs simulation using the conway_assignment_three function It takes
command-line parameters specifying the number of time steps, the size of the board, and the
starting configuration (blinker, glider, and random). 

Assignment3_script3 which runs simulation using conway_assignment_three function for 500 time steps using a board of size 1000x1000 with a random initial board state where the cells are
chosen to be alive with 50% probability. This script plots the number of alive and dead cells
This plot will be dynamic and will update after each time step. This graph created and updated using the Matplotlib library.

