import math
import numpy as np
import pygame

COLUMNS = 20
ROWS = 20

WIDTH = 25
HEIGHT = 25
WINDOW_SIZE = [WIDTH * ROWS, HEIGHT * COLUMNS]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    Run(COLUMNS, ROWS)

def Run(cols, rows):

    board = SetUpBoard(cols, rows)

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        DrawBoard(board, screen)
        clock.tick(60)
        pygame.display.flip()

        board = ManageStates(board)
        
    pygame.quit()

def SetUpBoard(cols, rows):
    board = [[np.random.randint(2) for row in range(rows)] for col in range(cols)]
    return board

def DrawBoard(board, screen):
    for row in range(len(board)):
        for column in range(len(board[0])):
            colour = WHITE
            if board[row][column] == 1:
                colour = BLACK
            pygame.draw.rect(screen,
                            colour,
                            [(WIDTH) * column,
                            (HEIGHT) * row,
                            WIDTH,
                            HEIGHT])

def ManageStates(board):
    temp = board.copy()

    for row in range(len(board)):
        for column in range(len(board[0])):
            currentState = temp[row][column]
            totalNeighbours = CountNeighbours(temp, row, column)
            board[row][column] = UpdateStates(currentState, totalNeighbours)
    return board

def UpdateStates(currentState, totalNeighbours):
    if currentState == 0 and totalNeighbours == 3:
        return 1
    elif currentState == 1 and (totalNeighbours < 2 or totalNeighbours > 3):
        return 0
    else:
        return currentState

def CountNeighbours(temp, x, y):
    sum = temp[x][y] * -1

    for i in range(-1, 2):
        for j in range(-1, 2):
            column = (x + i + COLUMNS) % COLUMNS
            row = (y + j + ROWS) % ROWS
            sum += temp[column][row]
    return sum

main()

