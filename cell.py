import pygame, random

from constants import ALIVE_COLOR, DEAD_COLOR


CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = 20, 20

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        # self.alive = random.choice([True, False, False, False])
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface(CELL_SIZE)
        self.rect = self.image.get_rect()
        self.cell_coordinate = (self.grid_x * CELL_WIDTH, self.grid_y * CELL_HEIGHT)
        self.neighbours = []

    def update(self):
        self.rect.topleft = self.cell_coordinate

    def draw(self):
        if self.alive:
            self.image.fill(DEAD_COLOR)
        else:
            self.image.fill(DEAD_COLOR)
            pygame.draw.rect(self.image, ALIVE_COLOR, (1, 1, 18, 18))

        self.surface.blit(self.image, self.cell_coordinate)

    def get_neighbours(self, grid):
        # list of numbers we can add to our position (self.grid_x, self.grid_y) to get neighbours' positions
        neighbour_list = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, -1], [0, 1], [1, 0], [-1, 0]]
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y

        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += 30
            if neighbour[1] < 0:
                neighbour[1] += 30

            if neighbour[0] > 29:
                neighbour[0] -= 30
            if neighbour[1] > 29:
                neighbour[1] -= 30

        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except:
                print(neighbour)
