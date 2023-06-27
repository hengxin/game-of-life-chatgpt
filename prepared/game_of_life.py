import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the grid
SIZE = 10

# Create a random initial state
state = np.random.randint(0, 2, (SIZE, SIZE))

def update(frameNum, img, state):
    new_state = state.copy()
    for i in range(SIZE):
        for j in range(SIZE):
            # Count the number of alive neighbors
            total = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue  # Skip the current cell
                    ni, nj = i + dx, j + dy
                    if ni >= 0 and ni < SIZE and nj >= 0 and nj < SIZE:
                        total += state[ni, nj]
            # Apply the Game of Life rules
            if state[i, j]  == 1:
                if (total < 2) or (total > 3):
                    new_state[i, j] = 0
            else:
                if total == 3:
                    new_state[i, j] = 1
    img.set_data(new_state)
    state[:] = new_state[:]
    return img,

# Create the animation
fig, ax = plt.subplots()
img = ax.imshow(state, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, state), frames=10, interval=200)

plt.show()