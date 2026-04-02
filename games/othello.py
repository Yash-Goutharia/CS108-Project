import pygame
import numpy as np
import sys

# Constants
BOARD_SIZE = 8
CELL_SIZE = 80
WIDTH = HEIGHT = BOARD_SIZE * CELL_SIZE
BLUE = (0, , 128)
BLACK = (200, 200, 0)
WHITE = (255, 255, 255)
HIGHLIGHT = (200, 0, 0)

# Directions (8 directions)
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0),  (1, 1)
]


class Othello:
    def __init__(self, player1="Player1", player2="Player2"):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

        # Initial setup
        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2

        self.current_player = 1  
        self.players = {1: player1, 2: player2}

    def switch_turn(self):
        self.current_player = 3 - self.current_player

    def on_board(self, x, y):
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    def get_valid_moves(self, player):
        valid_moves = []

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.board[x][y] != 0:
                    continue

                if self.is_valid_move(x, y, player):
                    valid_moves.append((x, y))

        return valid_moves

    def is_valid_move(self, x, y, player):
        opponent = 3 - player

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            found_opponent = False

            while self.on_board(nx, ny) and self.board[nx][ny] == opponent:
                nx += dx
                ny += dy
                found_opponent = True

            if found_opponent and self.on_board(nx, ny) and self.board[nx][ny] == player:
                return True

        return False

    def make_move(self, x, y, player):
        if not self.is_valid_move(x, y, player):
            return False

        self.board[x][y] = player
        opponent = 3 - player

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            tiles_to_flip = []

            while self.on_board(nx, ny) and self.board[nx][ny] == opponent:
                tiles_to_flip.append((nx, ny))
                nx += dx
                ny += dy

            if self.on_board(nx, ny) and self.board[nx][ny] == player:
                for fx, fy in tiles_to_flip:
                    self.board[fx][fy] = player

        return True

    def has_moves(self, player):
        return len(self.get_valid_moves(player)) > 0

    def game_over(self):
        return not (self.has_moves(1) or self.has_moves(2))

    def get_winner(self):
        black = np.sum(self.board == 1)
        white = np.sum(self.board == 2)

        if black > white:
            return self.players[1]
        elif white > black:
            return self.players[2]
        else:
            return "Draw"
