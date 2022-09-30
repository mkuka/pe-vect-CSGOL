# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:25:54 2022

@author: Kuka
"""
"""
This class creates time_steps using two different methods(vectorized and non 
 vectorized).Also return a list of board stages for given number of time steps

"""


from board import Game_Board
import numpy as np
import copy
from scipy import signal



class time_steps:
    def __init__(self, board,number_steps,method,add):
       self.board = board
       self.number_steps = number_steps
       self.method=method
       self.add=add

       # self.board_state_history()
       # if method=='vectorized':
       #     print(self.conway_assignment_three())
       # else:
       #     pass
            # self.conway_assignment_two()
    
    def list_pad(self):
        my_list=self.board
        
        rows = len(my_list)
        cols = len(my_list[0])
        padded_list =np.array([[0]*(cols+2)]*(rows+2)) 
        # padded_list=[[0]*(cols+2)]*(rows+2)
        padded_list[1:(rows+1),1:(cols+1)]=my_list
        # grid[3:3+len(glider_gun),3:3+len(glider_gun[0])]=glider_gun
        # padded_list[1:rows+1,1:cols+1] = my_list
        return padded_list
    
    """
    non vectorized method
    """
    def conway_assignment_two(self):
        
        size=len(self.board)
        sum_alive_neighbors=np.zeros((size, size))
        # print(sum_alive_neighbors[2][2])
        padded_board=self.list_pad()
        
        
        padded_row=len(padded_board)
        padded_col=len(padded_board[0])
        for i in range(1,(padded_row-1)):
            for j in range(1,padded_col-1):
                # alive_neighbors = sum(padded_board[i-1:i+1],padded_board[j-1:j+1])-padded_board[i][j]
                         
                alive_neighbors=0
                alive_neighbors = (padded_board[i-1][j-1], padded_board[i][j-1],
                                      padded_board[i+1][j-1], padded_board[i+1][j],
                                      padded_board[i+1][j+1], padded_board[i][j+1],
                                      padded_board[i-1][j+1], padded_board[i-1][j])
                # print(alive_neighbors)
                sum_alive_neighbors[i-1][j-1] = sum(alive_neighbors)
           
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                
        
                current_cell=self.board[i][j]
                
                # Each cell with three neighbors becomes populated.
                if current_cell==0:
                    if sum_alive_neighbors[i][j]==3 :
                        self.board[i][j]=1
                # Each cell with two or three neighbors survives.
                elif current_cell==1 and (sum_alive_neighbors[i][j]==2 or sum_alive_neighbors[i][j]==3 ):
                        self.board[i][j]=1
                elif current_cell==1:    
                    # Each cell with one or no neighbors dies.
                    # Each cell with four or more neighbors dies, as if by overpopulation.
                    if sum_alive_neighbors[i][j]>3 or sum_alive_neighbors[i][j]==1 or sum_alive_neighbors[i][j]==0 :
                        self.board[i][j]=0
        
       
        return self.board
    
    
    def Game_rules(b,board1,sum_alive_neighbors):
        # np.vectorize()
        # global Game_Board
        if board1==0:
            if sum_alive_neighbors==3 :
                # print(sum_alive_neighbors)
                return 1
        # Each cell with two or three neighbors survives.
        elif board1==1 and (sum_alive_neighbors==2 or sum_alive_neighbors==3 ):
                return 1
        elif board1==1:    
            # Each cell with one or no neighbors dies.
            # Each cell with four or more neighbors dies, as if by overpopulation.
            if sum_alive_neighbors>3 or sum_alive_neighbors==1 or sum_alive_neighbors==0 :
                return 0
        # print(board1)
        return board1
    
    """
    vectorized method
    """
    
    def conway_assignment_three(self):
       
        kernel=[[1,1,1],
                [1,0,1],
                [1,1,1]]
       
        board=np.array(self.board)
        bb=np.pad(board,pad_width=1)
        
        sum_alive_neighbors=np.zeros((len(self.board)))
        
        sum_alive_neighbors=signal.convolve2d(kernel, bb, "valid")
        
        board1=copy.deepcopy(board[0])
        vfunc = np.vectorize(self.Game_rules)
        
        return vfunc(board1,sum_alive_neighbors)
        # return sum_alive_neighbors
    """
    This function will take a parameter add which causes it to save the board state 
    for each time-step and return this board state history as a list.
    
    """
    def board_state_history(self):
        
        board_history=[]
        # print(n)
        for i in range(self.number_steps):
            board1=[]
            if self.method=='vectorized':
                # print('test',i)
                board1.insert(0,self.conway_assignment_three())
                # print(board1)
            else:
                board1.insert(0,self.conway_assignment_two())
                # print('222test')
            
            if self.add.lower()=='y':
            
                new_list = copy.deepcopy(board1[0])
                board_history.insert(i,new_list)
            
            self.board=board1[0]
        
                

        return board_history
    

    
           
    

