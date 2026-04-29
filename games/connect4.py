import numpy as np
import pygame
pygame.display.init()
pygame.font.init()
class connect4:
    def __init__(self,player_1,player_2):
        self.rows=7
        self.columns=7
        self.board=np.zeros((7,7),dtype = int)
        self.latest_move = [0,0]
        self.move_no = 1
        self.player_1 = player_1
        self.player_2 = player_2
    def Play_Move(self,Screen):
        Cell_size = 80
        left_seperation = (Screen.get_width() - 7*Cell_size)/2
        top_seperation = (Screen.get_height() - 7*Cell_size)/2
        x =0
        y =0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
            board_x = x - left_seperation
            board_y = y - top_seperation
            if 0<=board_x<(7*Cell_size) and 0<=board_y<(7*Cell_size):
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
    def win(self):
       if self.move_no%2==0:
          p = self.player_1
          q = self.player_2
       else:
          p = self.player_2
          q = self.player_2

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
       diag_line2 = np.diag(np.fliplr(self.board),k=(self.board.shape[1]-1-self.latest_move[0])-self.latest_move[1]) #second diagonal slice in opposite direction
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
             return [True,"Win","connect4",p,q]
       if np.sum(self.board == 0)==0:
          return [True,"Draw","connect4",self.player_1,self.player_2]
    
    def draw_game(self):
        return True
    def draw_board(self,Screen,image,d1,d2):
        Screen.fill("black")
        Screen.blit(image,(d1,d2))
        Cell_size = 80
        left_seperation=(Screen.get_width() - 7*Cell_size)/2
        top_seperation=(Screen.get_height() - 7*Cell_size)/2
        if self.move_no%2 != 0:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 7*Cell_size)/2 -60),60,(0,200,255),self.player_1,True,pygame.font.SysFont("Arial",28))
           self.draw_neon_button(Screen,30+int((7/2)*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 7*Cell_size)/2 -60),60,(0,200,255),self.player_2,False,pygame.font.SysFont("Arial",28))
        else:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 7*Cell_size)/2 -60),60,(0,200,255),self.player_1,False,pygame.font.SysFont("Arial",28))
           self.draw_neon_button(Screen,30+int((7/2)*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 7*Cell_size)/2 -60),60,(0,200,255),self.player_2,True,pygame.font.SysFont("Arial",28))
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
    def draw_neon_button(self,screen, x, y, w, h, color, text, active, font):
     radius = 1

     if active:
        for i in range(8):
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
