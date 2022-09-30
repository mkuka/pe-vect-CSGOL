# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:48:12 2022

@author: Kuka
"""
"""
A script which runs your simulation for a number of board sizes (starting at 1000x1000) and
increasing in increments of 250x250 up to the largest size you can simulate for 100 time steps.
This script will run both conway_assignment_two and conway_assignment_three functions.
This script will output a graph of the time steps per millisecond for each board size you attempt
for both the assignment three and assignment two implementations.
"""

from board import Game_Board
from step_history import time_steps
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

fig1= plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
# Game_Board=[[]]*size

def get_x_y(board1):
    # print(board1)
    j_x=[]
    i_y=[]
   
    for i in range(size):
        for j in range(size):
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

def visualize_states(states,ini_plot,fig):
    anim = FuncAnimation(fig, update_plot, frames=range(len(states)),fargs=(states,ini_plot,), interval=1000)
    return anim


def plot_timesteps_size(list1,list2,size_list):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(size_list,list1,color='red',marker='o')#non vectorized
    ax.plot(size_list,list2,color='blue',marker='v')#vectorized
    plt.ylabel('timsteps per millisecond')
    plt.xlabel('size')
    plt.xlim(min(size_list),max(size_list))
    plt.title('red-non vectorized & blue vectorized')
    # plt.legend('loop','vectorize',loc="upper left")
    plt.show()
    
    
# pattern=(input("Enter the initial state(glider gun/blinker/random/beacon) : "))
percentage_alive_cell=int(input("Enter the percentage of alive cells : "))
pattern='random'
# n=10
n=100
list_Ass2=[]
list_Ass3=[]

"""
for the quick result i used range(200,600,50) and 10 time steps for random

"""
# for size in range(200,600,50):
   
for size in range(1000,2000,250):
    new_Game_Board=Game_Board(size,'random',percentage_alive_cell,)

    new_board=(new_Game_Board.new_board_stage())


    with_loop_steps=time_steps(new_board,3,'loop','n')
    

    vectorized_steps=time_steps(new_board,3,'vectorized','n')
    
    xdata,ydata=get_x_y(new_board)    
    plot_board_A2=ax1.plot(xdata, ydata, color='blue', marker='X', linestyle='',markersize=12)[0]   
    plot_board_A3=ax2.plot(xdata, ydata, color='green', marker='X', linestyle='',markersize=12)[0]
    
    """
    elapsed time and frrequency calculation for non vectorized method
    """
    t1_start=time.time()*1000
    with_loop_history=with_loop_steps.board_state_history()
    visualize_states(with_loop_history,plot_board_A2,fig1)
    t1_end=time.time()*1000
    t_ass2=t1_end-t1_start
   
    # print('ass2',t_ass2)
    t2=n/t_ass2
    list_Ass2.append(t2)
    
    """
    elapsed time and frequency calculation for vectorized method
    """
    t2_start=time.time()*1000
    vectorized_history=vectorized_steps.board_state_history()
    visualize_states(vectorized_history,plot_board_A3,fig2)
    t2_end=time.time()*1000
    t_ass3=t2_end-t2_start
    # if t3!=0:
    t3=n/t_ass3
    # print('ass3',t_ass3)
    list_Ass3.append(t3)
    
    
    
# size_list=range(200,600,50)
size_list=range(1000,2000,250)

plot_timesteps_size(list_Ass2,list_Ass3,size_list)













