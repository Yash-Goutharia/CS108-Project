import numpy as np
import pygame
pygame.display.init()
pygame.font.init()
class connect4:
    def __init__(self):
        self.rows=7
        self.columns=7
        self.board=np.zeros((7,7),dtype = int)
        self.latest_move = [0,0]
        self.move_no = 1
    def Play_Move(self,Screen):
        Cell_size = 80
        left_seperation = (Screen.get_width() - 7*Cell_size)/2
        top_seperation = (Screen.get_height() - 7*Cell_size)/2
        x =0
        y =0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTON:
                    (x,y) = event.pos
            board_x = x + left_seperation
            board_y = y + top_seperation
            if 0<=board_x<(7*Cell_size) and 0<=board_x<(7*Cell_size):
                row = int(board_y//Cell_size)
                column = int(board_x//Cell_size)
                if row == 6 and self.board[row, column] == 0:
                    self.move_no = self.move_no + 1
                    self.latest_move = [row, column]
                    if self.move_no%2 ==0:
                        self.board[row, column]=2
                    else:
                        self.board[row,column]=1
                    break
                elif self.board[row, column] == 0 and self.board[row+1, column]!=0:
                    self.move_no = self.move_no + 1
                    self.latest_move = [row,column]
                    if self.move_no%2== 0:
                        self.board[row, column] = 2
                    else:
                        self.board[row, column]=1
                    break
        return None
    def win(self):
       if np.sum(self.board == 0)==0:
          if np.sum(self.board == 1)> np.sum(self.board == 2):
             return True
          elif np.sum(self.board == 1)< np.sum(self.board == 2):
             return True
          else:
             return self.draw_game()
       if self.move_no%2 != 0:
          winning_line=[1,1,1,1]
       else:
          winning_line=[2,2,2,2]
       current_row = self.latest_move[0]
       current_column = self.latest_move[1]
       diag_line1 = np.diag(self.board, k=self.latest_move[1]-self.latest_move[0]) #diagonal sliced array containing the latest played cell
       diag_line2 = np.diag(np.fliplr(self.board),k=(self.board.shape[1]-1-self.latest_move[1])-self.latest_move[0]) #second diagonal slice in opposite direction
       row_column_diagonal_slices = [#checking if the latest filled row contains a winning line 
                     self.board[current_row, 0:4],self.board[current_row, 1:5],
                     self.board[current_row, 2:6],self.board[current_row, 3:7],
                     #checking if the latest filled column contains a winning line 
                     self.board[0:4,current_column],self.board[1:5,current_column],
                     self.board[2:6,current_column],self.board[3:7,current_column],
                     #checking if the first\ diagonal contains a winning line
                     diag_line1[0:4],diag_line1[1:5],diag_line1[2:6],diag_line1[3:7],
                     #checking if the second/ diagonal contains a winning line
                     diag_line2[0:4],diag_line2[1:5],diag_line2[2:6],diag_line2[3:7],
                     ]
       for slice_arr in row_column_diagonal_slices:
          if np.array_equal(slice_arr,winning_line):
             return True
    def draw_game(self):
        return True
    def draw_board(self,Screen):
        Screen.fill("black")
        Cell_size = 80
        left_seperation=(Screen.get_width() - 7*Cell_size)/2
        top_seperation=(Screen.get_height() - 7*Cell_size)/2
        for i in range(7):
          for j in range(7):
             x = left_seperation + (i * Cell_size)
             y = top_seperation + (j * Cell_size)
             cell_center = (x + (Cell_size/2), y + (Cell_size/2))
             radius = (Cell_size * 3)/8 
             rect = (x,y,Cell_size,Cell_size)
             pygame.draw.rect(Screen,(255,255,255),rect)
             pygame.draw.rect(Screen,(0,200,0),rect,2)
             if self.board[j, i] == 1:
                pygame.draw.circle(Screen,(0,0,200),cell_center,radius)
             elif self.board[j, i] == 2:
                pygame.draw.circle(Screen, (200, 0, 0), cell_center, radius)
        pygame.display.update()

