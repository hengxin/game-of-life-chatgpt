import pygame
import time

# Grid size
WIDTH, HEIGHT = 10, 10

# Window size
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800

# Cell size
CELL_WIDTH = WINDOW_WIDTH // WIDTH
CELL_HEIGHT = WINDOW_HEIGHT // HEIGHT

# Colors
BACKGROUND_COLOR = (128, 0, 128)  # Purple
CELL_COLOR = (255, 255, 0)  # Yellow

# Initialize Pygame
pygame.init()

# Set up display
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Initial grid state
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Glider pattern
glider_pattern = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
for x, y in glider_pattern:
    grid[y][x] = 1

def draw_grid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            rect = pygame.Rect(x*CELL_WIDTH, y*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(WINDOW, CELL_COLOR if grid[y][x] else BACKGROUND_COLOR, rect)

def update_grid():
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            live_neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (dx != 0 or dy != 0) and (0 <= nx < WIDTH) and (0 <= ny < HEIGHT):
                        live_neighbors += grid[ny][nx]
            if grid[y][x] and live_neighbors in [2, 3]:
                new_grid[y][x] = 1
            elif not grid[y][x] and live_neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_grid()
    pygame.display.update()

    grid = update_grid()
    time.sleep(0.1)
