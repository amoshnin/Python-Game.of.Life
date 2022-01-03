import pygame
import copy
from cell import Cell

vec = pygame.math.Vector2

class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.rows = 30
        self.columns = 30
        self.grid = [[Cell(self.image, column, row) for column in range(self.columns)] for row in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((102, 102, 102))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, column, row) for column in range(self.columns)] for row in range(self.rows)]

    def evaluate(self):
        new_grid = copy.copy(self.grid)

        for row in self.grid:
            for cell in row:
                cell.live_neighbours()

        for yIdx, row in enumerate(self.grid):
            for xIdx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[yIdx][xIdx].alive = True
                    if cell.alive_neighbours < 2 and cell.alive:
                        new_grid[yIdx][xIdx].alive = False
                    if cell.alive_neighbours > 3 and cell.alive:
                        new_grid[yIdx][xIdx].alive = False
                else:
                    if cell.alive_neighbours == 3:
                        new_grid[yIdx][xIdx].alive = True
        self.grid = new_grid
