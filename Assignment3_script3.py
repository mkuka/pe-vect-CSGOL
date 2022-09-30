# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:36:24 2022

@author: Kuka
"""

"""
A script which runs your simulation using conway_assignment_three function for 500 time
steps using a board of size 1000x1000 with a random initial board state where the cells are
chosen to be alive with 50% probability. This script will plot the number of alive and dead cells
(they should sum to the number of cells in your board). This plot will be dynamic and will
update after each time step. This graph will be created and updated using the Matplotlib library.
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy import signal




def new_board_state(size,initial_states):
    choices=[1,0]
    alive=(int(50)/100)
    dead=1-alive
    # print(alive," ",dead)
    Game_Board=np.random.choice(choices, size*size, p=[alive,dead]).reshape(size, size)
    
    return Game_Board
    
    # return Game_Board


def Game_rules(Game_Board1,sum_alive_neighbors):
    # global Game_Board
    if Game_Board1==0:
        if sum_alive_neighbors==3 :
            # print(sum_alive_neighbors)
            return 1
    # Each cell with two or three neighbors survives.
    elif Game_Board1==1 and (sum_alive_neighbors==2 or sum_alive_neighbors==3 ):
            return 1
    elif Game_Board1==1:    
        # Each cell with one or no neighbors dies.
        # Each cell with four or more neighbors dies, as if by overpopulation.
        if sum_alive_neighbors>3 or sum_alive_neighbors==1 or sum_alive_neighbors==0 :
            return 0
    return Game_Board1
    

def conway_assignment_three(board):
    # if active_state==True:
    kernel=[[1,1,1],
            [1,0,1],
            [1,1,1]]
    # global Game_Board
    Game_board_with_pad=np.pad(board,pad_width=1)
    # for t_step in range(time_step):
    sum_alive_neighbors=np.zeros((board.shape))
    sum_alive_neighbors=signal.convolve2d(kernel, Game_board_with_pad, "valid")
    # print(sum_alive_neighbors)
    vfunc = np.vectorize(Game_rules)
    return vfunc(board,sum_alive_neighbors)
    
   



def get_cell_count(board1):
       
    number_alive_cell=sum(sum(board1))
    number_dead_cell=(size*size)-number_alive_cell
    return number_alive_cell,number_dead_cell
    


def update_three(frame):
    
    global Game_Board
    
    r_board=conway_assignment_three(Game_Board)
    number_alive_cell,number_dead_cell=get_cell_count(r_board)
   
    Game_Board=r_board
    ax.plot(frame,number_alive_cell,'x', color='blue')[0]
    ax.plot(frame,number_dead_cell,'o', color='red')[0]
    
    
    

if __name__=='__main__':
    size=1000
    n=500
    
    alive_cells=[]
    dead_cells=[]
    pattern='random'
    
    Game_Board=new_board_state(size,pattern)
    
    
   
    number_alive_cell,number_dead_cell=get_cell_count(Game_Board)
   
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # plt.xlim(0,n)
    # plt.ylim(0,1000000)
    plt.legend('alive','dead',loc="upper left")
    x=0
    plt.ylabel('cell count')
    plt.xlabel('time_steps')
    
    
    ax.plot(x,number_alive_cell,'x', color='blue')[0]
    ax.plot(x,number_dead_cell,'o', color='red')[0]
    
    plt.show()
    
    anim= FuncAnimation(fig, update_three, frames=range(n),interval=100)
                         
# ,fargs=(Game_Board,)