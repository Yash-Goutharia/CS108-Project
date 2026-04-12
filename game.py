import pygame
from games.tictactoe import tictactoe
from games.connect4 import connect4
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
#base class for execution of the game
class Board_Games:
    #class initialized
    def __init__(self,game,Screen):
        self.player1 = sys.argv[1]
        self.player2 = sys.argv[2]
        self.current_player = sys.argv[1]
        self.board_game = game
        self.gaming_screen = Screen
        self.start_game()
    #fucntion to switch turns
    def switch_turn(self):
        if self.current_player == sys.argv[1]:
            self.current_player = sys.argv[2]
        else:
            self.current_player = sys.argv[1]
    #funcyion to check if the current player won the game or not
    def won(self):
        if self.board_game.win():
            return True
    #function to start the gameplay
    ##draws the board after every turn each player makes a move and stops if a player wins or draws
    def start_game(self):
        while True:
            self.board_game.draw_board(self.gaming_screen)
            self.board_game.Play_Move(self.gaming_screen)
            self.switch_turn()
            if self.won():
                break
#initialized pygame module and the screen
pygame.display.init()
pygame.font.init()
Width = 1200
Height = 800
screen=pygame.display.set_mode((Width,Height))   

running = True

while(running):
    screen.fill("black")
    button_Width = 300
    button_Height = 60

    ### tictactoe buttton to go to tictactoe game
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
    
    ######Othello button to go to Othello game
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

    #to write text as name of games inside the buttons with a font
    font = pygame.font.SysFont("trebuchetms",40)
    tictactoe_font = font.render("Tic-Tac-Toe",True,(255,255,255))
    screen.blit(tictactoe_font, (Width/2 - button_Width/2 + 50,300))
    othello_font = font.render("Othello",True,(255,255,255))
    screen.blit(othello_font, (Width/2 - button_Width/2 + 85,420))
    connect4_font = font.render("Connect4",True,(255,255,255))
    screen.blit(connect4_font, (Width/2 - button_Width/2 + 70,540))
    
    my_game = None
    #to select the game the players want to play
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if tictactoe_button.collidepoint(mouse_pos):
                my_game = Board_Games(tictactoe(),screen)
            elif othello_button.collidepoint(mouse_pos):
                pass
            elif connect4_button.collidepoint(mouse_pos):
                my_game = Board_Games(connect4(),screen)
    
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

pygame.quit()

