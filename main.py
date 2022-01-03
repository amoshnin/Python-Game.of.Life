# Rules of the game: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# It is a grid of cells.
# Each cell in that grid knows if it is alive or dead.
# If the cell is:
#   alive = it will be black
#   dead = it will be white
# Every frame/iteration, there is a set of rules that determine whether a cell stays alive or dies or becomes alive

import pygame
import sys

WIDTH, HEIGHT = 800, 800
BACKGROUND = (42, 21, 13)
FPS = 60

def get_event():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def update():
    pass

def draw():
    window.fill(BACKGROUND)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    get_event()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.exit()
sys.exit()