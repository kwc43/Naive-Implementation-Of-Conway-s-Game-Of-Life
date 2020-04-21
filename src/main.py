import math
import numpy as np
import pygame

cols = 20
rows = 20

WIDTH = 25
HEIGHT = 25
WINDOW_SIZE = [WIDTH * rows, HEIGHT * cols]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    DrawBoard(SetUpBoard(cols, rows))

def SetUpBoard(cols, rows):
    board = [[np.random.randint(2) for row in range(rows)] for col in range(cols)]
    return board
    
def DrawBoard(board):  
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        for row in range(rows):
            for column in range(cols):
                colour = WHITE
                if board[row][column] == 1:
                    colour = BLACK
                pygame.draw.rect(screen,
                             colour,
                             [(WIDTH) * column,
                              (HEIGHT) * row,
                              WIDTH,
                              HEIGHT])
        clock.tick(60)
        pygame.display.flip()
        
    pygame.quit()

main()

