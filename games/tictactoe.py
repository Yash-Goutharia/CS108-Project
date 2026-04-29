import numpy as np
import pygame
pygame.display.init()
pygame.font.init()
class tictactoe:
    #initialized tictactoe class
    def __init__(self,player_1,player_2):
        self.rows = 10
        self.columns = 10
        self.board = np.zeros((10,10),dtype = int)
        self.latest_move = [0, 0] #the latest [row,col] played in game by the player.
        self.move_no = 1 #total no. of moves played till now + 1 / current move no.
        self.player_1 = player_1
        self.player_2 = player_2
    def Play_Move(self,Screen):
        Cell_size=50
        left_seperation = (Screen.get_width() - 10 * Cell_size)/2 #board distance from left edge of screen
        top_seperation = (Screen.get_height() - 10 * Cell_size)/2 #board distance from top edge of screen
        x = 0
        y = 0

        while True:
         for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN:
              (x, y) = event.pos
         #x and y coordinates in board's frame
         board_x = x - left_seperation
         board_y = y - top_seperation

         # if a board cell is clicked for playing a move
         if 0 <= board_x < (10 * Cell_size) and 0 <= board_y < (10 * Cell_size):
        
         # to get cell coordinates/cell position wrt board
            column = int(board_x // Cell_size)
            row = int(board_y // Cell_size)
            
         # to see if that cell is already played in board or not
         #if a move is not played in that cell, it is represented by zero, otherwise 1 or 2 depending on which player is moving
   
            if self.board[row, column] == 0:
               self.move_no = self.move_no + 1
               self.latest_move = [row, column]
               if self.move_no%2 !=0:
                 self.board[row, column] = 1
               else:
                 self.board[row, column] = 2
               break 
         return None
    
    def win(self):
       if self.move_no%2==0:
          p = self.player_1
          q = self.player_2
       else:
          p = self.player_2
          q = self.player_1

       if self.move_no%2 != 0:
          winning_line=[1,1,1,1,1]
       else:
          winning_line=[2,2,2,2,2]
       current_row = self.latest_move[0]
       current_column = self.latest_move[1]
       diag_line1 = np.diag(self.board, k=self.latest_move[1]-self.latest_move[0]) #diagonal sliced array containing the latest played cell
       diag_line2 = np.diag(np.fliplr(self.board),k=(self.board.shape[1]-1-self.latest_move[0])-self.latest_move[1]) #second diagonal slice in opposite direction
       row_column_diagonal_slices = [#checking if the latest filled row contains a winning line 
                     self.board[current_row, 0:5],self.board[current_row, 1:6],
                     self.board[current_row, 2:7],self.board[current_row, 3:8],
                     self.board[current_row, 4:9],self.board[current_row, 5:10],
                     #checking if the latest filled column contains a winning line 
                     self.board[0:5,current_column],self.board[1:6,current_column],
                     self.board[2:7,current_column],self.board[3:8,current_column],
                     self.board[4:9,current_column],self.board[5:10,current_column],
                     #checking if the first\ diagonal contains a winning line
                     diag_line1[0:5],diag_line1[1:6],diag_line1[2:7],
                     diag_line1[3:8],diag_line1[4:9],diag_line1[5:10],
                     #checking if the second/ diagonal contains a winning line
                     diag_line2[0:5],diag_line2[1:6],diag_line2[2:7],
                     diag_line2[3:8],diag_line2[4:9],diag_line2[5:10]
                     ]
       for slice_arr in row_column_diagonal_slices:
          if np.array_equal(slice_arr,winning_line) and len(slice_arr)==5:
             return [True,"Win","tictactoe",p,q]
       if np.sum(self.board == 0)==0:
          return [True,"Draw","tictactoe",self.player_1,self.player_2]
    def draw_board(self,Screen,image,d1,d2):
        Screen.fill("black")
        Screen.blit(image,(d1,d2))
        Cell_size = 50
        left_seperation=(Screen.get_width() - 10*Cell_size)/2
        top_seperation=(Screen.get_height() - 10*Cell_size)/2
        if self.move_no%2 != 0:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 10*Cell_size)/2 -60),60,(0,200,255),self.player_1,True,pygame.font.SysFont("Arial",35))
           self.draw_neon_button(Screen,30+int(5*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 10*Cell_size)/2 -60),60,(0,200,255),self.player_2,False,pygame.font.SysFont("Arial",35))
        else:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 10*Cell_size)/2 -60),60,(0,200,255),self.player_1,False,pygame.font.SysFont("Arial",35))
           self.draw_neon_button(Screen,30+int(5*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 10*Cell_size)/2 -60),60,(0,200,255),self.player_2,True,pygame.font.SysFont("Arial",35))
        for i in range(10):
          for j in range(10):
             x = left_seperation + (i * Cell_size)
             y = top_seperation + (j * Cell_size)
             rect = (x, y, Cell_size, Cell_size)

             pygame.draw.rect(Screen, (200,200 ,200), rect)      
             pygame.draw.rect(Screen, (0, 0, 0), rect, 2)         

             cell_center = (x + (Cell_size/2), y + (Cell_size/2))
             gap = Cell_size / 4 

             if self.board[j, i] == 1: 
                pygame.draw.line(Screen, (255, 0, 0), (x + gap, y + gap), (x + Cell_size - gap, y + Cell_size - gap), 4)
                pygame.draw.line(Screen, (255, 0, 0), (x + Cell_size - gap, y + gap), (x + gap, y + Cell_size - gap), 4)

             elif self.board[j, i] == 2:
                pygame.draw.circle(Screen, (0, 0, 0), cell_center, (Cell_size/2) - gap, 4)
        pygame.display.update()
    def draw_neon_button(self,screen, x, y, w, h, color, text, active, font):
     
     radius = 1
     if active:
        for i in range(4):
            alpha = max(10, 120 - i * 15)
            glow = pygame.Surface((w + i*10, h + i*10), pygame.SRCALPHA)
            pygame.draw.rect(glow, (*color, alpha),
                             (0, 0, w + i*10, h + i*10),
                             border_radius=radius + i*5)
            screen.blit(glow, (x - i*5, y - i*5))

        body = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(body, (*color, 40), (0, 0, w, h), border_radius=radius)
        screen.blit(body, (x, y))

        pygame.draw.rect(screen, color, (x, y, w, h), width=2, border_radius=radius)

        highlight = pygame.Surface((w, h//2), pygame.SRCALPHA)
        pygame.draw.rect(highlight, (255, 255, 255, 30),
                         (0, 0, w, h//2), border_radius=radius)
        screen.blit(highlight, (x, y))

        text_color = (255, 255, 255)
     else:
        pygame.draw.rect(screen, (40, 40, 40), (x, y, w, h), border_radius=radius)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h), width=2, border_radius=radius)
        text_color = (150, 150, 150)

     txt = font.render(text, True, text_color)
     txt_rect = txt.get_rect(center=(x + w//2, y + h//2))
     screen.blit(txt, txt_rect)
    