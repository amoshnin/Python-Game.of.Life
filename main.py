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

# Rules in pseudo-code:
# Each square has neighbours and rules that come with number of "live" neighbours:
# - live cell with fewer than two live neighbours = dead cell
# - live cell with more than three live neighbours = dead cell
# - live cell with two or three live neighbours = live cell
# - dead cell with three live neighbours = live cell

import sys
import pygame
from constants import BOARD_SIZE, BOARD_WIDTH, BOARD_HEIGHT, BACKGROUND, FPS, PAUSED, RUNNING, SETTING
from game_window import GameWindow
from button import Button

# --------- --------- --------- Setting functions
def setting_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def setting_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def setting_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

# --------- --------- --------- Running functions
def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    if frame_count % (FPS//10) == 0:
        game_window.evaluate()

def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

# --------- --------- --------- Paused functions
def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

# --------- --------- --------- Other functions

def mouse_on_grid(position):
    if position[0] > 100 and position[0] < BOARD_WIDTH - 100:
        if position[1] > 180 and position[1] < BOARD_HEIGHT - 20:
            return True
    return False

def click_cell(position):
    grid_pos = [position[0] - 100, position[1] - 180]
    grid_pos[0], grid_pos[1] = grid_pos[0] // 20, grid_pos[1] // 20

    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

pygame.init()
window = pygame.display.set_mode(BOARD_SIZE)
clock = pygame.time.Clock()
game_window = GameWindow(window, 100, 180)


def run_game():
    global state
    state = RUNNING

def pause_game():
    global state
    state = PAUSED

def reset_game():
    global state
    state = SETTING
    game_window.reset_grid()

def make_buttons():
    buttons = []
    buttons.append(Button(window, BOARD_WIDTH // 2 - 50, 50, 100, 30, text="RUN", color=(28, 111, 51), hover_color=(48, 131, 81), bold_text=True, function=run_game, state=SETTING))
    buttons.append(Button(window, BOARD_WIDTH // 2 - 50, 50, 100, 30, text="PAUSE", color=(18,104,135), hover_color=(51, 168, 212), bold_text=True, function=pause_game, state=RUNNING))
    buttons.append(Button(window, BOARD_WIDTH // 4 - 50, 50, 100, 30, text="RESET", color=(117, 14,14), hover_color=(217, 54,54), bold_text=True, function=reset_game, state=PAUSED))
    buttons.append(Button(window, BOARD_WIDTH // 1.25 - 50, 50, 100, 30, text="RESUME", color=(28,111,51), hover_color=(48, 131, 81), bold_text=True, function=run_game, state=PAUSED))
    return buttons

buttons = make_buttons()
state = SETTING
frame_count = 0

running = True
while running:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()
    if state == SETTING:
        setting_get_events()
        setting_update()
        setting_draw()

    if state == RUNNING:
        running_get_events()
        running_update()
        running_draw()

    if state == PAUSED:
        paused_get_events()
        paused_update()
        paused_draw()

    pygame.display.update()
    clock.tick(FPS)
    print(state)

pygame.exit()
sys.exit()
