import pygame
import sys  # Add this import at the top of your file
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
grid = set()

# Glider pattern
glider_pattern = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
for x, y in glider_pattern:
    grid.add((x, y))

def draw_grid():
    if not grid:
        return

    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)

    grid_width = max_x - min_x + 1
    grid_height = max_y - min_y + 1

    cell_width = WINDOW_WIDTH // grid_width
    cell_height = WINDOW_HEIGHT // grid_height

    for x, y in grid:
        rect = pygame.Rect((x-min_x)*cell_width, (y-min_y)*cell_height, cell_width, cell_height)
        pygame.draw.rect(WINDOW, CELL_COLOR, rect)

def update_grid():
    new_grid = set()
    candidates = grid.union((x+dx, y+dy) for x, y in grid for dx in [-1, 0, 1] for dy in [-1, 0, 1])

    for x, y in candidates:
        live_neighbors = sum((nx, ny) in grid for nx in [x-1, x, x+1] for ny in [y-1, y, y+1] if (nx, ny) != (x, y))
        if (x, y) in grid and live_neighbors in [2, 3]:
            new_grid.add((x, y))
        elif (x, y) not in grid and live_neighbors == 3:
            new_grid.add((x, y))

    return new_grid

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_grid()
    pygame.display.update()

    grid = update_grid()
    time.sleep(2)
