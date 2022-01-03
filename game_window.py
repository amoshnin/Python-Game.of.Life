import pygame
from cell import Cell

vec = pygame.math.Vector2

class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.rows = 10
        self.columns = 10
        self.grid = [[Cell(self.image, column, row) for column in range(self.columns)] for row in range(self.rows)]

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