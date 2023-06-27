import random
import time

def create_grid():
  grid = []
  for i in range(10):
    row = []
    for j in range(10):
      row.append(random.randint(0, 1))
    grid.append(row)
  return grid

def update_grid(grid):
  new_grid = []
  for i in range(10):
    row = []
    for j in range(10):
      neighbors = 0
      for di in range(-1, 2):
        for dj in range(-1, 2):
          if 0 <= i + di < 10 and 0 <= j + dj < 10:
            neighbors += grid[i + di][j + dj]
      if grid[i][j] == 1 and (neighbors == 2 or neighbors == 3):
        new_grid.append(1)
      elif grid[i][j] == 0 and neighbors == 3:
        new_grid.append(1)
      else:
        new_grid.append(0)
  return new_grid

def draw_grid(grid):
  for i in range(10):
    for j in range(10):
      if grid[i][j] == 1:
        print('\033[4;33m█\033[0m', end='')
      else:
        print('\033[4;35m  \033[0m', end='')
    print()

def main():
  grid = create_grid()
  draw_grid(grid)
  for i in range(100):
    grid = update_grid(grid)
    draw_grid(grid)
    time.sleep(0.5)

if __name__ == '__main__':
  main()