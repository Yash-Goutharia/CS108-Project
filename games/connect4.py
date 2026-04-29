import numpy as np
import pygame
pygame.display.init()
pygame.font.init()

class connect4:
    def __init__(self):
        self.rows = 7
        self.columns = 7
        self.board = np.zeros((7,7), dtype=int)
        self.latest_move = [0,0]
        self.move_no = 1

    def Play_Move(self, Screen):

        Cell_size = 80
        left_sep = (Screen.get_width() - 7*Cell_size)/2
        top_sep = (Screen.get_height() - 7*Cell_size)/2

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                board_x = x - left_sep
                board_y = y - top_sep

                if 0 <= board_x < (7*Cell_size) and 0 <= board_y < (7*Cell_size):

                    column = int(board_x // Cell_size)

                    # drop piece to lowest empty row
                    for row in range(self.rows-1, -1, -1):
                        if self.board[row, column] == 0:

                            if self.move_no % 2 != 0:
                                self.board[row, column] = 1
                            else:
                                self.board[row, column] = 2

                            self.latest_move = [row, column]
                            self.move_no += 1
                            break

        return None

    def win(self):

        player = 1 if self.move_no % 2 == 0 else 2

        # check horizontal, vertical, diagonal
        for r in range(self.rows):
            for c in range(self.columns):

                if c+3 < self.columns:
                    if all(self.board[r, c+i] == player for i in range(4)):
                        return True

                if r+3 < self.rows:
                    if all(self.board[r+i, c] == player for i in range(4)):
                        return True

                if r+3 < self.rows and c+3 < self.columns:
                    if all(self.board[r+i, c+i] == player for i in range(4)):
                        return True

                if r-3 >= 0 and c+3 < self.columns:
                    if all(self.board[r-i, c+i] == player for i in range(4)):
                        return True

        # draw
        if np.sum(self.board == 0) == 0:
            return True

        return False

    def draw_board(self, Screen):

        Screen.fill("black")

        Cell_size = 80
        left_sep = (Screen.get_width() - 7*Cell_size)/2
        top_sep = (Screen.get_height() - 7*Cell_size)/2

        for i in range(self.columns):
            for j in range(self.rows):

                x = left_sep + i * Cell_size
                y = top_sep + j * Cell_size

                rect = (x, y, Cell_size, Cell_size)
                pygame.draw.rect(Screen, (255,255,255), rect)
                pygame.draw.rect(Screen, (0,200,0), rect, 2)

                center = (x + Cell_size/2, y + Cell_size/2)
                radius = Cell_size // 3

                if self.board[j, i] == 1:
                    pygame.draw.circle(Screen, (0,0,200), center, radius)

                elif self.board[j, i] == 2:
                    pygame.draw.circle(Screen, (200,0,0), center, radius)

        # small UI hint
        font = pygame.font.Font(None, 30)
        text = font.render("Press Q to quit", True, (255,255,255))
        Screen.blit(text, (10,10))

        pygame.display.update()
