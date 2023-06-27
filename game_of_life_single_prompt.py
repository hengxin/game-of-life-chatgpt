import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

class GameOfLife:
    def __init__(self, N=100):
        self.N = N
        self.grid = np.random.choice([0,1], N*N, p=[0.9, 0.1]).reshape(N, N)

    def update(self, frameNum, img, grid, N):
        newGrid = grid.copy()
        for i in range(N):
            for j in range(N):
                total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                             grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] +
                             grid[(i+1)%N, (j+1)%N])/255)
                if grid[i, j]  == 1:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = 0
                else:
                    if total == 3:
                        newGrid[i, j] = 1
        img.set_data(newGrid)
        grid[:] = newGrid[:]
        return img,

    def generate(self):
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self.update, fargs=(img, self.grid, self.N, ),
                                      frames = 10,
                                      interval=200,
                                      save_count=50)
        plt.show()

if __name__ == '__main__':
    game = GameOfLife(N = 100)
    game.generate()
