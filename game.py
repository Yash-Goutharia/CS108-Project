import pygame
from games.tictactoe import tictactoe
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
class Board_Games:
    def __init__(self,game):
        self.player1 = sys.argv[1]
        self.player2 = sys.argv[2]
        self.current_player = sys.argv[1]
        if game == "tictactoe":
            self.board_game = tictactoe()
    def switch_turn(self):
        if self.current_player == sys.argv[1]:
            self.current_player = sys.argv[2]
        else:
            self.current_player = sys.argv[1]
    def won(self):
        if self.board_game.win():
            return True

pygame.init()
Width = 1200
Height = 800
screen=pygame.display.set_mode((Width,Height))

def main_menu():

    button_Width = 300
    button_Height = 60

    # tictactoe buttton to go to tictactoe game
    tictactoe_btn = pygame.Surface((button_Width, button_Height))
    for i in range(button_Height):
       t = (i / button_Height)* (9/10)  
       g = int(255 * (1 - t))   
       r = 0
       b = 0
       pygame.draw.line(tictactoe_btn, (r, g, b), (0, i), (button_Width, i))
    mask = pygame.Surface((button_Width, button_Height), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255,255,255), (0,0,button_Width,button_Height), border_radius=30)
    tictactoe_btn.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(tictactoe_btn, (Width/2 - button_Width/2, 300))
    tictactoe_button = pygame.Rect(Width/2 - button_Width/2,300,button_Width,button_Height)
    pygame.draw.rect(screen, (255,255,255), (Width/2 - button_Width/2,300,button_Width,button_Height), 3, border_radius=30)
    pygame.draw.rect(screen, (0,0,0), (Width/2 - button_Width/2,300,button_Width,button_Height), 1, border_radius=30)
    
    #Othello button to go to Othello game
    Othello_btn = pygame.Surface((button_Width, button_Height))
    for i in range(button_Height):
       t = (i / button_Height)* (9/10)  
       r = int(255 * (1 - t))   
       g = 0
       b = 0
       pygame.draw.line(Othello_btn, (r, g, b), (0, i), (button_Width, i))
    mask = pygame.Surface((button_Width, button_Height), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255,255,255), (0,0,button_Width,button_Height), border_radius=30)
    Othello_btn.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(Othello_btn, (Width/2 - button_Width/2, 420))
    othello_button = pygame.Rect(Width/2 - button_Width/2,420,button_Width,button_Height)
    pygame.draw.rect(screen, (255,255,255), (Width/2 - button_Width/2,420,button_Width,button_Height), 3, border_radius=30)
    pygame.draw.rect(screen, (0,0,0), (Width/2 - button_Width/2,420,button_Width,button_Height), 1, border_radius=30)

    #connect4 button to go to connect4 game
    Connect4_btn = pygame.Surface((button_Width, button_Height))
    for i in range(button_Height):
       t = (i / button_Height)* (9/10)  
       b = int(255 * (1 - t))   
       r = 0
       g = 0
       pygame.draw.line(Connect4_btn, (r, g, b), (0, i), (button_Width, i))
    mask = pygame.Surface((button_Width, button_Height), pygame.SRCALPHA)
    pygame.draw.rect(mask, (255,255,255), (0,0,button_Width,button_Height), border_radius=30)
    Connect4_btn.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(Connect4_btn, (Width/2 - button_Width/2, 540))
    connect4_button = pygame.Rect(Width/2 - button_Width/2,540,button_Width,button_Height)
    pygame.draw.rect(screen, (255,255,255), (Width/2 - button_Width/2,540,button_Width,button_Height), 3, border_radius=30)
    pygame.draw.rect(screen, (0,0,0), (Width/2 - button_Width/2,540,button_Width,button_Height), 1, border_radius=30)

    #to write text as name of games inside the buttons
    font = pygame.font.SysFont("trebuchetms",40)
    tictactoe = font.render("Tic-Tac-Toe",True,(255,255,255))
    screen.blit(tictactoe, (Width/2 - button_Width/2 + 50,300))
    othello = font.render("Othello",True,(255,255,255))
    screen.blit(othello, (Width/2 - button_Width/2 + 85,420))
    connect4 = font.render("Connect4",True,(255,255,255))
    screen.blit(connect4, (Width/2 - button_Width/2 + 70,540))
    
    #to select the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if tictactoe_button.collidepoint(mouse_pos):
                return "tictactoe"
            elif othello_button.collidepoint(mouse_pos):
                return "othello"
            elif connect4_button.collidepoint(mouse_pos):
                return "connect4"
def Quit():
    pass
running = True

while(running):
    game = main_menu()
    x = Board_Games(game)
    x.board_game.draw_board()
    while True:
        if Quit:
            break
        x.board_game.Play_Move()
        x.board_game.draw_board()
        x.switch_player()
        if x.won() or x.draw():
            break
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

pygame.quit()

