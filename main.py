# Rules of the game: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Each cell in that grid knows if it is alive or dead.
# If the cell is:
#   alive = it will be black
#   dead = it will be white
# Every frame/iteration/frame of game loop, there is a set of rules
# that determine whether a cell (stays alive) or (dies) or (becomes alive)
# Rules are:
#   1. any live cell with fewer than two live neighbours dies, as if it's underpopulated/starvation
#   2. any live cell with two or three alive neighbours stays alive and survives the next generation
#   3. any cell that is surrounded by more than three live neighbours, it dies by overpopulation
#   4. any dead cell becomes alive if there are exactly three neighbours around it, representing reproduction

# With these 4 simple rules, we obtain a lot of interesting patterns (ex: Still lifes, Oscillators, Spaceships)
# Patterns in Game of Life = https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life

import sys
import pygame
from constants import BOARD_SIZE, BACKGROUND, FPS
from game_window import GameWindow


def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def update():
    game_window.update()

def draw():
    window.fill(BACKGROUND)
    game_window.draw()

pygame.init()
window = pygame.display.set_mode(BOARD_SIZE)
clock = pygame.time.Clock()
game_window = GameWindow(window, 100, 180)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.exit()
sys.exit()
