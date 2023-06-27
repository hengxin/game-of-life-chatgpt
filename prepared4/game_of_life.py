import pygame
import numpy as np
import os

# Set up some constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def load_rle(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Skip comment lines
    lines = [line for line in lines if not line.startswith('#')]

    # Parse the header
    header = lines[0].strip().split(', ')
    width = int(header[0].split(' = ')[1])
    height = int(header[1].split(' = ')[1])

    # Initialize the grid
    grid = np.zeros((height, width))

    # Parse the pattern
    row = 0
    col = 0
    for line in lines[1:]:
        i = 0
        while i < len(line):
            run_count = ''
            while i < len(line) and line[i].isdigit():
                run_count += line[i]
                i += 1
            run_count = int(run_count) if run_count else 1
            if i < len(line):
                if line[i] == 'b':
                    col += run_count
                elif line[i] == 'o':
                    for _ in range(run_count):
                        grid[row, col] = 1
                        col += 1
                elif line[i] == '$':
                    row += run_count
                    col = 0
                i += 1

    return grid

# Load the initial pattern from an RLE file
filename = '../1beacon.rle'  # Replace with the path to your RLE file
grid = load_rle(filename)

# Colors
PURPLE = (128, 0, 128)  # RGB for purple
YELLOW = (255, 255, 0)  # RGB for yellow

def draw_window(grid):
    rows, cols = grid.shape
    square_size = min(WIDTH // cols, HEIGHT // rows)

    # Fill the background with purple
    WIN.fill(PURPLE)

    for i in range(rows):
        for j in range(cols):
            color = YELLOW if grid[i, j] else PURPLE
            pygame.draw.rect(WIN, color, pygame.Rect(j*square_size, i*square_size, square_size, square_size))

    # Draw x-y axes
    pygame.draw.line(WIN, WHITE, (0, 0), (WIDTH, 0))  # x-axis
    pygame.draw.line(WIN, WHITE, (0, 0), (0, HEIGHT))  # y-axis

    # Draw labels
    font = pygame.font.Font(None, 32)
    for i in range(rows):
        label = font.render(str(i), 1, WHITE)
        WIN.blit(label, (5, i * square_size))
    for j in range(cols):
        label = font.render(str(j), 1, WHITE)
        WIN.blit(label, (j * square_size, 5))

    pygame.display.update()

def update(grid):
    # Check for life on the edges of the grid
    if np.any(grid[0, :]) or np.any(grid[-1, :]) or np.any(grid[:, 0]) or np.any(grid[:, -1]):
        # Add a border of dead cells around the current grid
        grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # Count the number of alive neighbors
            total = np.sum(grid[max(i-1, 0):min(i+2, rows), max(j-1, 0):min(j+2, cols)]) - grid[i, j]

            # Apply the rules of the game
            if grid[i, j] == 1 and (total < 2 or total > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and total == 3:
                new_grid[i, j] = 1

    return new_grid

def main():
    clock = pygame.time.Clock()
    run = True

    # Iterate over the RLE files in the "patterns" directory
    for filename in os.listdir('../patterns'):
        if filename.endswith('.rle'):
            # Load the initial pattern from the RLE file
            grid = load_rle(os.path.join('../patterns', filename))

            # Run the Game of Life for 15 steps
            for _ in range(15):
                if run:
                    clock.tick(2)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                    grid = update(grid)
                    draw_window(grid)
                    pygame.display.set_caption(filename)  # Show the name of the pattern in the title of the window

    pygame.quit()

if __name__ == "__main__":
    main()