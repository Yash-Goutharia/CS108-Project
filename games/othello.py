import numpy as np
import pygame
pygame.display.init()
pygame,font.init()
class tictactoe:
    #initialised othello.py class
    def __init__(self):
        self.rows = 8
        self.coloumns = 8
        self.board = np.zeros((8,8),dtype = int)
        self.latest_move = [0,0] 
        self.move_no = 1


        #initial 4 discs
        self.board[3,3] = 2
        self.board[4,4] = 2
        self.board[3,4] = 1
        self.board[4,3] = 1

    
    def Play_Move(self,Screen):
        Cell_size = 60
        left_seperation = (Screen.get_width() - 8 * Cell_size)/2 #SEPEARTION FROM LEFT 
        top_seperation = (Screen.get_height() - 8 * Cell_size)/2 #SEPERATION FROM RIGHT
        x = 0 
        y =0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
            #x and y coordinates in board's ref frame
            board_x = x - left_seperation
            board_y = y - top_seperation

            #if a borad cell is clicked for move
            if 0 <= board_x < (10*Cell_size) and 0 <= board_y < (10*Cell_size):

            #to get cell coordinates wrt board 
                coloumn = int(board_x//Cell_size)
                row = int(board_y// Cell_size)


        # to see if that cell is already played in board or not
        # if a move is not played in that cell, it is represented by zero, otherwise 1 or 2 depending on which player is moving
        
        if self.board[row,column] == 0:
            self.move_no = self.move_no + 1
            self.latest_move = [row, coloumn]
            if self.move_no%2 !=0:
                self.board[row, coloumn] = 1
            else:
                self.board[row, coloumn] = 2
            break
        return None
    def win(self):
        if np.sum(self.board == 0) == 0:
            if np.sum(self.board == 1 ) > np.sum(self.board == 2):
                return True
            else:
    def draw_board(self):
      pass
