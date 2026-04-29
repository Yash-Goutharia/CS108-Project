import numpy as np
import pygame
pygame.display.init()
pygame.font.init()
class othello:
    #initialised othello.py class
    def __init__(self,player_1,player_2):
        self.rows = 8
        self.coloumns = 8
        self.board = np.zeros((8,8),dtype = int)
        self.latest_move = [0,0] 
        self.move_no = 1
        self.player_1 = player_1
        self.player_2 = player_2
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    
                    # Coordinate transformation to board space
                    board_x = x - left_seperation
                    board_y = y - top_seperation

                    # Check if click is inside the 8x8 grid
                    if 0 <= board_x < (8 * Cell_size) and 0 <= board_y < (8 * Cell_size):
                        column = int(board_x // Cell_size)
                        row = int(board_y // Cell_size)

                        # Determine current player: 1 (Black) starts, then 2 (White)
                        current_player = 1 if self.move_no % 2 == 0 else 2
                        
                        # Logic: Check if cell is empty AND if the move is valid in Othello
                        if self.board[row][column] == 0:
                            flipped_discs = self.get_flipped_discs(row, column, current_player)
                            
                            if flipped_discs:
                                self.board[row][column] = current_player
                                for r, c in flipped_discs:
                                    self.board[r][c] = current_player
                                
                                self.move_no += 1
                                self.latest_move = [row, column]
                                return True 
            pygame.display.update()

    def get_flipped_discs(self, row, col, player):
        """Helper to find which opponent pieces would be flipped by this move."""
        opponent = 2 if player == 1 else 1
        discs_to_flip = []
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            potential_flips = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                potential_flips.append((r, c))
                r += dr
                c += dc
            
            # If we hit our own color after a line of opponent discs, it's a valid outflank
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                discs_to_flip.extend(potential_flips)
        
        return discs_to_flip
    def is_valid_move(self ,row, col, player):
        DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),(0, 1),
        (1, -1),  (1, 0), (1, 1)]
        if self.board[row][col] != 0:
           return False

        opponent = 2 if player == 1 else 1

        for dr, dc in DIRECTIONS:
            r, c = row + dr, col + dc
            found_opponent = False

            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                found_opponent = True
                r += dr
                c += dc

            if found_opponent and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                  return True

        return False

    def has_valid_move(self,player):
       for i in range(8):
          for j in range(8):
            if self.is_valid_move(i, j, player):
                 return True
       return False

    def any_valid_move(self,p):
         return self.has_valid_move(p)

    def win(self):
        if np.sum(self.board == 0) == 0 or (not self.any_valid_move(1) and not self.any_valid_move(2):
            if np.sum(self.board == 1 ) > np.sum(self.board == 2):
                return [True,"Win","othello",self.player_1,self.player_2]
            elif np.sum(self.board == 2) > np.sum(self.board == 1):
                return [True,"Win","othello",self.player_2,self.player_1]
            else:
                return [True,"Draw","othello",self.player_1,self.player_2]
    def draw_board(self,Screen,image,d1,d2):
        Screen.fill("black")
        Screen.blit(image,(d1,d2))
        Cell_size = 75
        left_seperation=(Screen.get_width() - 8*Cell_size)/2
        top_seperation=(Screen.get_height() - 8*Cell_size)/2
        if self.move_no%2 != 0:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 8*Cell_size)/2 -60),60,(0,200,255),self.player_1,True,pygame.font.SysFont("Arial",35))
           self.draw_neon_button(Screen,30+int(4*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 8*Cell_size)/2 -60),60,(0,200,255),self.player_2,False,pygame.font.SysFont("Arial",35))
        else:
           self.draw_neon_button(Screen,30+int((Screen.get_width()-image.get_width())/2),int(Screen.get_height()/2),int((image.get_width()- 8*Cell_size)/2 -60),60,(0,200,255),self.player_1,False,pygame.font.SysFont("Arial",35))
           self.draw_neon_button(Screen,30+int(4*Cell_size + (Screen.get_width()/2)),int(Screen.get_height()/2),int((image.get_width()- 8*Cell_size)/2 -60),60,(0,200,255),self.player_2,True,pygame.font.SysFont("Arial",35))
        for i in range(8):
          for j in range(8):
             x = left_seperation + (i * Cell_size)
             y = top_seperation + (j * Cell_size)
             rect = (x, y, Cell_size, Cell_size)

             pygame.draw.rect(Screen, (0,255 , 0), rect)      
             pygame.draw.rect(Screen, (0, 0, 150), rect, 2)         

             cell_center = (x + (Cell_size/2), y + (Cell_size/2))
             gap = Cell_size / 5 

             if self.board[j, i] == 1: 
                pygame.draw.circle(Screen, (0, 0, 0), cell_center, (Cell_size/2) - gap)

             elif self.board[j, i] == 2:
                pygame.draw.circle(Screen, (255, 255, 255), cell_center, (Cell_size/2) - gap)
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
