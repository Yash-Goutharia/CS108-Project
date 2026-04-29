import sys
import pygame
from othello import othello
from connect4 import connect4
from tictactoe import tictactoe

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game Hub")

font = pygame.font.Font(None, 40)

# get players from main.sh
if len(sys.argv) >= 3:
    p1 = sys.argv[1]
    p2 = sys.argv[2]
else:
    p1 = "Player1"
    p2 = "Player2"


def show_menu():
    while True:
        screen.fill((0, 0, 0))

        title = font.render("Select Game", True, (255,255,255))
        opt1 = font.render("1. Othello", True, (255,255,255))
        opt2 = font.render("2. Connect4", True, (255,255,255))
        opt3 = font.render("3. Tictactoe", True, (255,255,255))
        opt4 = font.render("4. Quit", True, (255,255,255))

        screen.blit(title, (200, 150))
        screen.blit(opt1, (200, 250))
        screen.blit(opt2, (200, 300))
        screen.blit(opt3, (200, 350))
        screen.blit(opt4, (200, 400))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "othello"
                if event.key == pygame.K_2:
                    return "connect4"
                if event.key == pygame.K_3:
                    return "tictactoe"
                if event.key == pygame.K_4:
                    return None
            



def run_othello():
    game = othello()

    running = True
    while running:

        game.draw_board(screen)

        # handle move
        game.Play_Move(screen)

        # check win
        if game.win():
            print("Game Over")
            pygame.time.wait(2000)
            return
        
def run_connect4():
    game = connect4()

    while True:
        game.draw_board(screen)

        result = game.Play_Move(screen)

        if result == "quit":
            return

        if game.win():
            print("Game Over")
            pygame.time.wait(2000)
            return

def run_tictactoe():
    game = tictactoe()

    running = True
    while running:

        game.draw_board(screen)

        # handle move
        game.Play_Move(screen)

        # check win
        if game.win():
            print("Game Over")
            pygame.time.wait(2000)
            return
        

# MAIN LOOP
while True:
    choice = show_menu()

    if choice is None:
        break

    if choice == "othello":
        run_othello()

    if choice == "connect4":
        run_connect4()

    if choice == "tictactoe":
        run_tictactoe()

pygame.quit()
