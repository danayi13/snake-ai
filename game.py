import pygame
import sys
import time

from board import Board

WINDOW_DIM = 1000

# TODO get better colors
MENU_BAR_COLOR = (125, 197, 248)
BOARD_BACKGROUND_COLOR = (171, 243, 225)

UPDATE_SPEED_SECONDS = 1

if __name__ == "__main__":

    board = Board(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else Board()

    # Window Setup 
    pygame.init()
    pygame.display.set_caption("Dana's Snake Game")
    screen = pygame.display.set_mode((WINDOW_DIM,WINDOW_DIM))
    screen.fill(MENU_BAR_COLOR)
    pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, [0, WINDOW_DIM * 0.2, WINDOW_DIM, WINDOW_DIM * 0.85])       
    done = False

    # Run Game
    while not done:    
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:    
                done = True    

        # Update Screen
        board.draw_board(screen)
        pygame.display.flip()  
        time.sleep(UPDATE_SPEED_SECONDS)
    
    pygame.quit()
