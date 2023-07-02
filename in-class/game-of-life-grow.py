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

    # Draw x-axis
    for x in range(WIDTH):
        text = pygame.font.Font(None, 24).render(str(x), True, (255, 255, 255))
        WINDOW.blit(text, (x*CELL_WIDTH, 0))

    # Draw y-axis
    for y in range(HEIGHT):
        text = pygame.font.Font(None, 24).render(str(y), True, (255, 255, 255))
        WINDOW.blit(text, (WINDOW_WIDTH - CELL_WIDTH, y*CELL_HEIGHT))

def update_grid():
    global WIDTH, HEIGHT  # Make WIDTH and HEIGHT modifiable
    new_grid = [[0 for _ in range(WIDTH+2)] for _ in range(HEIGHT+2)]  # Create a larger grid
    for y in range(HEIGHT):
        for x in range(WIDTH):
            live_neighbors = sum(grid[(y+dy)%HEIGHT][(x+dx)%WIDTH] for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0)
            if grid[y][x] and live_neighbors in [2, 3]:
                new_grid[y+1][x+1] = 1  # Offset by 1 to account for the larger grid
            elif not grid[y][x] and live_neighbors == 3:
                new_grid[y+1][x+1] = 1  # Offset by 1 to account for the larger grid
    WIDTH, HEIGHT = WIDTH + 2, HEIGHT + 2  # Update WIDTH and HEIGHT
    return new_grid

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_grid()
    pygame.display.update()

    grid = update_grid()
    CELL_WIDTH = WINDOW_WIDTH // WIDTH  # Update CELL_WIDTH
    CELL_HEIGHT = WINDOW_HEIGHT // HEIGHT  # Update CELL_HEIGHT
    time.sleep(1)
