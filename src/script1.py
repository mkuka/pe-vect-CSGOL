
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:13:36 2022

@author: Kuka
"""
"""
a function which calls conway_two. This function will contain a loop. Each
iteration through this loop will represent a single time-step of our simulation. This function will
take a parameter which causes it to save the board state for each time-step and return this board
state history as a list.
 Do the same with script3 without loop here this script using convolve2d from scipy
 and vectorize from numpy
"""
from board import Game_Board
from step_history import time_steps
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = fig.add_subplot(111)
# Game_Board=[[]]*size


def get_x_y(board1):
    j_x=[]
    i_y=[]
   
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            # print(_board[i][j])
                       
            if (board1[i][j]==1):
                    
                j_x.append(j)
                i_y.append(i)
    return j_x,i_y 


if __name__=='__main__':
    size=int(input("Enter the board size : "))
    pattern=(input("Enter the initial state(glider gun/random) : "))
    n=int(input("Enter the number of symulation you need : "))
    percentage_alive_cell=int(input("Enter the percentage of alive cells : "))
    
    
    new_Game_Board=Game_Board(size,pattern,percentage_alive_cell,)

    new_board=(new_Game_Board.new_board_stage())


    with_loop_steps=time_steps(new_board,n,'loop','y')
    

    vectorized_steps=time_steps(new_board,n,'vectorized','y')
    
    
    
    xdata,ydata=get_x_y(new_board)
    
    
    plot_board_A2=ax.plot(xdata, ydata, color='blue', marker='X', linestyle='',markersize=8)[0]
    plt.title('non vectorized')
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    plot_board_A3=ax1.plot(xdata, ydata, color='green', marker='X', linestyle='',markersize=8)[0]
    plt.title('vectorized')
    store=str(input("Do you want to save this stage of board Y/N ?")) 
    
    
    with_loop_history=with_loop_steps.board_state_history()
    
    vectorized_history=vectorized_steps.board_state_history()
    
    
    # print(board_states_3)
    # plt.show()
    

def update_plot(frame,board_states,ini_plot):
    
    xdata, ydata=get_x_y(board_states[frame])
        # print(xdata)
    ini_plot.set_xdata(xdata)
    ini_plot.set_ydata(ydata)
    



anim = FuncAnimation(fig, update_plot, frames=range(len(with_loop_history)),fargs=(with_loop_history,plot_board_A2,), interval=1000)

anim2 = FuncAnimation(fig1, update_plot, frames=range(len(vectorized_history)),fargs=(vectorized_history,plot_board_A3,), interval=1000)

plt.show()

