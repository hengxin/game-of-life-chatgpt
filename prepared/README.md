# Conway's Game of Life in Python

This Python program simulates Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## How it Works

The program uses matplotlib to animate the Game of Life. It starts by loading an initial configuration from a Run Length Encoded (RLE) file. The RLE format is a compact way to represent the initial configuration of a Game of Life pattern.

The game rules are applied in the `update` function, which is called for each frame of the animation. The rules are applied to each cell in the grid, and the new state is displayed.

The program iterates over each RLE file in a specified directory, displaying the animation of the pattern stored in the RLE file for 15 steps. The name of the pattern is displayed in the title bar of the window.

## Code Structure

- `load_rle(filename)`: This function loads an RLE file and returns a numpy array representing the initial configuration of the Game of Life grid.
- `update(data)`: This function applies the Game of Life rules to the grid. It's called for each frame of the animation.
- The main part of the program is a loop that iterates over each RLE file in a directory. For each file, it loads the initial configuration, creates a matplotlib figure and axes, sets the window title to the pattern name, and creates a FuncAnimation to animate the Game of Life.

## How to Run

To run the program, simply execute the Python script. Make sure you have the required dependencies installed (numpy and matplotlib), and that you have some RLE files in the specified directory.

## Possible Improvements

- **Performance**: The current implementation could be optimized for larger patterns. For example, the Game of Life rules could be implemented using convolution, which would be faster for large grids.
- **Interactivity**: The program could be made interactive, allowing the user to pause the animation, manually advance the game by one step, or change the speed of the animation.
- **Editing**: The user could be allowed to edit the Game of Life grid while the game is paused, adding or removing cells.
- **Different Rules**: The program could be extended to support different sets of rules, not just the standard Game of Life rules.

## Contribute

We welcome contributions to this project! Whether you're interested in improving the code, adding new features, or just fixing a bug, your help is appreciated. Feel free to fork the project and submit a pull request with your changes.