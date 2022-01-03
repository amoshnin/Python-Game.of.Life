import pygame

from constants import ALIVE_COLOR, DEAD_COLOR


CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = 20, 20

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface(CELL_SIZE)
        self.rect = self.image.get_rect()
        self.cell_coordinate = (self.grid_x * CELL_WIDTH, self.grid_y * CELL_HEIGHT)

    def update(self):
        self.rect.topleft = self.cell_coordinate

    def draw(self):
        if self.alive:
            self.image.fill(DEAD_COLOR)
        else:
            self.image.fill(DEAD_COLOR)
            pygame.draw.rect(self.image, ALIVE_COLOR, (2, 2, 18, 18))

        self.surface.blit(self.image, self.cell_coordinate)
