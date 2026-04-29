import numpy as np
import pygame
pygame.display.init()
pygame.font.init()
font = pygame.font.Font(None, 36)
class othello:
    #initialised othello.py class
    def __init__(self):
        self.rows = 8
        self.coloumns = 8
        self.board = np.zeros((8,8),dtype = int)
        self.latest_move = [0,0] 
        self.move_no = 1


        #initial 4 discs
        self.board[3,3] = 1
        self.board[4,4] = 1
        self.board[3,4] = 2
        self.board[4,3] = 2

    
    def Play_Move(self, Screen):
        Cell_size = 60
        left_sep = (Screen.get_width() - 8 * Cell_size)/2
        top_sep = (Screen.get_height() - 8 * Cell_size)/2

        x, y = 0, 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = event.pos

            board_x = x - left_sep
            board_y = y - top_sep

            if 0 <= board_x < (8 * Cell_size) and 0 <= board_y < (8 * Cell_size):

                col = int(board_x // Cell_size)
                row = int(board_y // Cell_size)

                if self.board[row, col] == 0:
                    player = 1 if self.move_no % 2 != 0 else 2

                    flipped = self.flip_discs(row, col, player)

                    if flipped:  # only valid move if something flips
                        self.board[row, col] = player
                        self.latest_move = [row, col]
                        self.move_no += 1
                        break

        return None
   
   
    def win(self):
        # game ends when board full OR no moves possible (simple version)
        if np.sum(self.board == 0) == 0:
            p1 = np.sum(self.board == 1)
            p2 = np.sum(self.board == 2)

            if p1 > p2:
                print("Player 1 wins")
                return True
            elif p2 > p1:
                print("Player 2 wins")
                return True
            else:
                return self.draw_game()
        return False
       
    def draw_game(self):
        print("Draw")
        return True

    def flip_discs(self, row, col, player):
        opponent = 2 if player == 1 else 1
        flipped_any = False

        directions = [
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
        ]

        for dx, dy in directions:
            r, c = row + dx, col + dy
            temp = []

            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r,c] == opponent:
                    temp.append((r,c))
                elif self.board[r,c] == player:
                    for (tr,tc) in temp:
                        self.board[tr,tc] = player
                    if len(temp) > 0:
                        flipped_any = True
                    break
                else:
                    break

                r += dx
                c += dy

        return flipped_any


    def draw_board(self, Screen):
        Screen.fill("black")

        Cell_size = 60
        left_sep = (Screen.get_width() - 8 * Cell_size)/2
        top_sep = (Screen.get_height() - 8 * Cell_size)/2

        for i in range(8):
            for j in range(8):
                x = left_sep + (i * Cell_size)
                y = top_sep + (j * Cell_size)

                rect = (x, y, Cell_size, Cell_size)

                pygame.draw.rect(Screen, (0,150,0), rect)
                pygame.draw.rect(Screen, (0,0,0), rect, 2)

                center = (x + Cell_size/2, y + Cell_size/2)

                if self.board[j,i] == 1:
                    pygame.draw.circle(Screen, (255,255,255), center, Cell_size/2 - 8)

                elif self.board[j,i] == 2:
                    pygame.draw.circle(Screen, (0,0,0), center, Cell_size/2 - 8)

        pygame.display.update()



# to run the individual file uncomment
# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((600,600))
#     pygame.display.set_caption("Othello")

#     game = othello()

#     while True:
#         game.draw_board(screen)
#         game.Play_Move(screen)

#         if game.win():
#             pygame.time.wait(2000)
#             break

#     pygame.quit()
