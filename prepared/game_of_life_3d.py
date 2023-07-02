import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Initialize a 3D grid with random values
N = 20
grid = np.random.choice([0, 1], N*N*N, p=[0.9, 0.1]).reshape(N, N, N)

def update(data):
    global grid
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                # Compute 3D slice for neighbor sum
                x1 = max(0, i-1)
                x2 = min(N-1, i+1)
                y1 = max(0, j-1)
                y2 = min(N-1, j+1)
                z1 = max(0, k-1)
                z2 = min(N-1, k+1)
                total = np.sum(grid[x1:x2+1, y1:y2+1, z1:z2+1]) - grid[i, j, k]
                # Apply rules
                if grid[i, j, k]  == 1:
                    if (total < 2) or (total > 3):
                        newGrid[i, j, k] = 0
                else:
                    if total == 3:
                        newGrid[i, j, k] = 1
    grid = newGrid

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def animate(i):
    ax.clear()
    update(i)
    ax.scatter(*np.where(grid==1), color='blue')
    ax.set_xlim([0, N])
    ax.set_ylim([0, N])
    ax.set_zlim([0, N])

ani = animation.FuncAnimation(fig, animate, frames=10, interval=200, repeat=False)

plt.show()