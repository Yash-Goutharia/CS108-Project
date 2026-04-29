import pygame
from games.tictactoe import tictactoe
from games.connect4 import connect4
from games.othello import othello
import numpy as np
import matplotlib.pyplot as plt
import sys
import subprocess
import datetime
import csv
#base class for execution of the game
class Board_Games:
    #class initialized
    def __init__(self,game,Screen,background,X_corner,Y_corner):
        self.player1 = sys.argv[1]
        self.player2 = sys.argv[2]
        self.current_player = sys.argv[1]
        self.board_game = game
        self.gaming_screen = Screen
        self.my_background = background
        self.X_1 = X_corner
        self.Y_1 = Y_corner
        self.start_game()
    #fucntion to switch turns
    def switch_turn(self):
        if self.current_player == sys.argv[1]:
            self.current_player = sys.argv[2]
        else:
            self.current_player = sys.argv[1]
    #function to start the gameplay
    def start_game(self):
        while True:
            self.board_game.draw_board(self.gaming_screen,self.my_background,self.X_1,self.Y_1)
            self.board_game.Play_Move(self.gaming_screen)
            self.switch_turn()
            result = self.board_game.win()
            if result is not None:
                if result[0] == True:
                    self.results_recording(result)
                    break
    def results_recording(self,result_list):
        game = [result_list[1],result_list[2],result_list[3],result_list[4]]
        with open("history.csv","a",newline='') as file:
            data =csv.writer(file)        
            data.writerow(game)
        self.leaderboard_analytics(game)
    def leaderboard_analytics(self,game_results):
        running = True
        Screen = self.gaming_screen
        while running:
            Screen.fill("black")
            self.gaming_screen.blit(self.my_background,(self.X_1,self.Y_1))
            x,y = 600,200
            font = pygame.font.SysFont("arial", 48)
            if game_results[0] == "Win":
                winner = game_results[2]
            if game_results[0] == "Win":
                text1 = font.render(f"{winner} won !", True, (255,255,255))
            else:
                text1 =font.render("Draw !",True,(255,255,255))
            text2 = font.render("Sort the leaderboard by:",True,(255,255,255))
            text_rect = text1.get_rect(center = (x,y))
            text_rect_2 = text2.get_rect(center = (x,y+100))
            Screen.blit(text1,text_rect)
            Screen.blit(text2,text_rect_2)
            win_sort = pygame.Rect(200,400,200,100)
            loss_sort = pygame.Rect(500,400,200,100)
            W_L_sort = pygame.Rect(800,400,200,100) 
            self.draw(Screen,win_sort,"Wins",font)
            self.draw(Screen,loss_sort,"Losses",font)
            self.draw(Screen,W_L_sort,"W/L ratio",font)
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if win_sort.collidepoint(mouse_pos):
                         sorted = "Win"
                         clicked = True
                         break
                    elif loss_sort.collidepoint(mouse_pos):
                         sorted = "Loss"
                         clicked = True
                         break
                    elif W_L_sort.collidepoint(mouse_pos):
                         sorted = "W/L"
                         clicked = True
                         break
            pygame.display.update()
            if clicked == True:
                break
        if sorted == "Win":
            subprocess.run(["bash","leaderboard.sh","2"])
        elif sorted == "Loss":
            subprocess.run(["bash","leaderboard.sh","3"])
        elif sorted == "W/L":
            subprocess.run(["bash","leaderboard.sh","4"])
        self.visual_graphs()
    def visual_graphs(self):
        wins = {}
        with open("history.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row)>0:
                  if row[0] == "Win":
                    winner = row[2]
                    wins[winner] = wins.get(winner, 0) + 1
                    wins[row[3]] = wins.get(row[3],0)
        players = list(wins.keys())
        win_counts = list(wins.values())
    
     #  Bar Chart
        plt.figure()
        plt.bar(players, win_counts)
        plt.xlabel("Players")
        plt.ylabel("Wins")
        plt.title("Leaderboard - Wins")
        plt.show()

       #Pie Chart
        plt.figure()
        plt.pie(win_counts, labels=players, autopct="%1.1f%%")
        plt.title("Win Distribution")
        plt.show()
        self.play_new_game()
    def draw(self,screen, rect, text, font):
       GLOW_COLOR = (70,170,255)
       RADIUS = 10
       BASE_COLOR = (0,100,100)
       TEXT_COLOR = (255,255,255)
       pygame.draw.rect(screen, GLOW_COLOR, rect.inflate(4, 4), border_radius=RADIUS)
       pygame.draw.rect(screen, BASE_COLOR, rect, border_radius=RADIUS)

       txt = font.render(text, True, TEXT_COLOR)
       screen.blit(txt, txt.get_rect(center=rect.center))
    def play_new_game(self):
       running = True
       Screen = self.gaming_screen
       while running:
            Screen.fill("black")
            Screen.blit(self.my_background,(self.X_1,self.Y_1))
            x,y = 600,200
            font = pygame.font.SysFont("arial", 48)
            text = font.render("Do you want to play another game ?", True, (255,255,255))
            text_rect = text.get_rect(center = (x,y))
            Screen.blit(text,text_rect)
            Yes_btn = pygame.Rect(300,400,200,100)
            No_btn = pygame.Rect(700,400,200,100)
            self.draw(Screen,Yes_btn,"Yes",font)
            self.draw(Screen,No_btn,"No",font)
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if Yes_btn.collidepoint(mouse_pos):
                         clicked = True
                         break
                    elif No_btn.collidepoint(mouse_pos):
                        pygame.quit()
            pygame.display.update()
            if clicked == True:
                break
       return 
#initialized pygame module and the screen
pygame.display.init()
pygame.font.init()
Width = 1200
Height = 800
screen=pygame.display.set_mode((Width,Height))
my_main_menu = pygame.image.load('main_menu.jpeg')
my_background = pygame.image.load('background.jpeg')
menu_width = my_main_menu.get_width()
menu_Height = my_main_menu.get_height()
background_width = my_background.get_width()
background_Height = my_background.get_height()
(X1,Y1) = ((Width - menu_width)/2 , (Height - menu_Height)/2)
(X2,Y2) = ((Width - background_width)/2, (Height - background_Height)/2)
running = True

while(running):
    screen.fill("black")
    screen.blit(my_main_menu,(X1,Y1))
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
                my_game = Board_Games(tictactoe(sys.argv[1],sys.argv[2]),screen,my_background,X2,Y2)
            elif othello_button.collidepoint(mouse_pos):
                my_game = Board_Games(othello(sys.argv[1],sys.argv[2]),screen,my_background,X2,Y2)
            elif connect4_button.collidepoint(mouse_pos):
                my_game = Board_Games(connect4(sys.argv[1],sys.argv[2]),screen,my_background,X2,Y2)
    
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

pygame.quit()

