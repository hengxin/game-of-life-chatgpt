import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def load_rle(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line for line in lines if not line.startswith("#") and not line.startswith("x =")]
        rle_string = "".join(lines).strip()

    grid = []
    row = []
    count = ""
    for char in rle_string:
        if char.isdigit():
            count += char
        elif char in "bo$!":
            if count == "":
                count = "1"
            if char == "b":
                row.extend([0] * int(count))
            elif char == "o":
                row.extend([1] * int(count))
            elif char == "$":
                grid.append(row)
                row = []
            elif char == "!":
                break
            count = ""
    if row:
        grid.append(row)

    # Pad shorter rows with dead cells
    max_length = max(len(row) for row in grid)
    grid = [row + [0] * (max_length - len(row)) for row in grid]

    return np.array(grid)

def update(data):
    global grid
    global mat
    global fig
    # Check the edges and add new rows/columns if necessary
    if np.any(grid[0, :]):
        grid = np.pad(grid, ((1, 0), (0, 0)), mode='constant')
    if np.any(grid[-1, :]):
        grid = np.pad(grid, ((0, 1), (0, 0)), mode='constant')
    if np.any(grid[:, 0]):
        grid = np.pad(grid, ((0, 0), (1, 0)), mode='constant')
    if np.any(grid[:, -1]):
        grid = np.pad(grid, ((0, 0), (0, 1)), mode='constant')

    newGrid = grid.copy()
    N, M = grid.shape  # Update the grid size
    for i in range(N):
        for j in range(M):
            # Calculate the boundaries considering the actual neighbors
            top = max(0, i - 1)
            bottom = min(N - 1, i + 1)
            left = max(0, j - 1)
            right = min(M - 1, j + 1)

            total = np.sum(grid[top:bottom + 1, left:right + 1]) - grid[i, j]

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    # Clear the previous plot and redraw
    plt.clf()
    mat = plt.matshow(newGrid, fignum=False)
    grid = newGrid
    return [mat]

# Directory containing the RLE files
directory = "../patterns"

# Iterate over each RLE file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".rle"):
        # Load the initial configuration from the RLE file
        grid = load_rle(os.path.join(directory, filename))

        print(filename)

        fig, ax = plt.subplots()

        pattern_name = filename.replace(".rle", "")
        fig.canvas.manager.set_window_title(pattern_name)

        mat = ax.matshow(grid)
        ani = animation.FuncAnimation(fig, update, frames=15, interval=500, save_count=50)
        plt.show(block=False)
        plt.pause(15 * 0.5)  # pause for the duration of the animation
        plt.close()  # close the figure