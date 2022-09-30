# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:03:30 2022

@author: Kuka
"""

"""
This class creates board fro given pattern and size.
"""

import numpy as np


class Game_Board:
    def __init__(self, size, initial_stage,percentage):
       self.size = size
       self.initial_stage = initial_stage
       self.percentage=percentage
       self.new_board_stage()
    
    def beacon_stage(self):
       # global Game_Board
       # grid = np.zeros((size, size))
       # grid=np.array([[0]*size]*size)
       Game_Board = [[0] * self.size]*self.size
       Game_Board=np.array(Game_Board)
      
       beacon = [[0, 0, 1, 1],
                 [0, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 0, 0]]
       x=(self.size-len(beacon))//2
       Game_Board[x:x+len(beacon),x:x+len(beacon[0])]=beacon
       # grid[3:3+len(blinker),3:3+len(blinker[0])]=blinker
       return Game_Board.tolist()

    def blinker_stage(self):
        
       # global Game_Board
       
         Game_Board=np.array([[0]*self.size]*self.size)
         blinker =[[0,0,0],
                   [0,1,0],
                   [0,1,0],
                   [0,1,0],
                   [0,0,0]]
         x=(self.size-len(blinker))//2
         Game_Board[x:x+len(blinker),x:x+len(blinker[0])]=blinker
       
         return Game_Board.tolist()
     
    def random_stage(self):
       # global Game_Board
       choices=[1,0]
       alive=(int(self.percentage)/100)
       dead=1-alive
       # print(alive," ",dead)
       Game_Board=np.random.choice(choices, self.size*self.size, p=[alive,dead]).reshape(self.size, self.size)
       
       return Game_Board.tolist()

    def glider_gun_stage(self):
       # global Game_Board
       if(self.size>45):
           
           grid=np.array([[0]*self.size]*self.size)
           # grid = np.zeros((size, size))
          
           # glider_gun = [[1,0,0],
           #               [0,1,1],
           #               [1,1,1]]
           
           glider_gun=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
           # grid[3][3+len(glider_gun),3:3+len(glider_gun[0])]=glider_gun
           x=(self.size-len(glider_gun[0]))//2
           # y=(size-len(glider_gun))//2
           # (size-len(glider_gun)//2)
           grid[x:x+len(glider_gun),x:x+len(glider_gun[0])]=glider_gun
           # grid[size-len(glider_gun):len(glider_gun),size-len(glider_gun[0]):len(glider_gun[0])]=glider_gun
           return grid.tolist()
       else:
           print('size must be more than 45 for glider gun state')
    
      
    def new_board_stage(self):
        Game_Board=[[]]*self.size
        if self.initial_stage=='blinker':
            Game_Board=self.blinker_stage()
        elif self.initial_stage=='random':
            Game_Board=self.random_stage()
        elif self.initial_stage=='glider gun':
            Game_Board=self.glider_gun_stage()
        elif self.initial_stage=='beacon':
            Game_Board=self.beacon_stage()
        return Game_Board
    
    def __repr__(self):
        return self
    
    # def to_list(board):
    #     # new_board=board
    #     # self.new_board_stage()
    #     rows = len(board)
    #     cols = len(board[0])
    #     new_board =np.array([[0]*cols]*(rows)) 
    #     # padded_list=[[0]*(cols+2)]*(rows+2)
    #     new_board[0:(rows),0:(cols)]=board
    #     # grid[3:3+len(glider_gun),3:3+len(glider_gun[0])]=glider_gun
    #     # padded_list[1:rows+1,1:cols+1] = my_list
    #     return new_board
  

   
     
   
   
   

   
    


  