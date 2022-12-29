# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:13:36 2022

@author: Kuka


"""
"""
A script that runs your simulation using the conway_three function. It will take
command-line parameters specifying the number of time steps, the size of the board, and the
starting configuration (blinker, glider, and random). This ought to be the function you use to
test your code. There will be an additional command-line parameter which animates the board
states.

python Ass3_script4.py -s 50 -n 5 -p random -per 50 -yes
"""
from board import Game_Board
from step_history import time_steps
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy import signal
import argparse
import copy



def get_x_y(board1):
    j_x=[]
    i_y=[]
    r=len(board1)
    c=len(board1[0])
    for i in range(r):
        for j in range(c):
            # print(_board[i][j])
                       
            if (board1[i][j]==1):
                    
                j_x.append(j)
                i_y.append(i)
    return j_x,i_y 

def update_plot(frame,board_states,ini_plot):
    
    xdata, ydata=get_x_y(board_states[frame])
        # print(xdata)
    ini_plot.set_xdata(xdata)
    ini_plot.set_ydata(ydata)



if __name__=='__main__':
   
    parser = argparse.ArgumentParser(description="Conway's game of life symulation" )
    parser.add_argument('-s', '--size',type=int,required=True,help='Size of the board')
    parser.add_argument('-n', '--number_of_symulation',type=int,required=True,help='How many time do you want symulate this model')
    parser.add_argument('-p', '--pattern',type=str,required=True,help='Specify the in itial stage of the board')
    parser.add_argument('-per', '--percentage',type=int,required=False,help='Percentage of life cell in the initial stage of the board')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-yes','--animate',action='store_true',help='save/not the stage of board')
    args=parser.parse_args()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    new_Game_Board=Game_Board(args.size,args.pattern,args.percentage)
    new_board=(new_Game_Board.new_board_stage())
    xdata,ydata=get_x_y(new_board)
    plot_board=ax.plot(xdata, ydata, color='blue', marker='X', linestyle='',markersize=5)[0]
    
    vectorized_steps=time_steps(new_board,3,'vectorized','y')
    vectorized_history=vectorized_steps.board_state_history()
if args.animate:
    # anim = FuncAnimation(fig, update_p, frames=range(args.number_of_symulation),interval=1000)
    anim = FuncAnimation(fig, update_plot, frames=range(len(vectorized_history)),fargs=(vectorized_history,plot_board,), interval=1000)                    
    plt.show()




    





