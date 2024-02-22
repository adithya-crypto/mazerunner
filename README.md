## Maze Solver
This repository contains a Python program to solve mazes using various search algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), and A*.
## Overview
The project consists of Python scripts that can generate and solve mazes using different search algorithms. It provides a command-line interface for users to select the maze difficulty level and the algorithm they want to use for solving the maze.
## Components
* 		Imagetostructure.py:
    * This script is responsible for converting maze images into graph structures that represent the maze.
    * It uses libraries such as OpenCV and scikit-image for image processing and skeletonization.
    * The image function reads an input maze image, preprocesses it, and returns a skeletonized image of the maze.
    * The TreeGeneration function generates a graph representation (networkx graph) of the skeletonized maze.
* 		Algos.py:
    * This script contains implementations of various search algorithms for solving the maze.
    * The implemented algorithms include Breadth-First Search (BFS), Depth-First Search (DFS), and A* search.
    * Each algorithm function takes the start and end points of the maze, the maze graph, and an optional parameter for display, and returns the path and number of steps taken to solve the maze.
* 		Display.py:
    * This script handles visualization and set creation for displaying the solved maze.
    * The SetCreator function creates a set of coordinates representing the solved path in the maze.
    * The Plot function visualizes the solved maze using matplotlib.
* 		Project.py:
    * This script serves as the main entry point for the program.
    * It provides a menu-driven interface for users to select the maze difficulty level and the search algorithm.
    * Based on user input, it calls the appropriate functions to solve the maze and visualize the solution.
## Usage
Users can run the Project.py script and follow the on-screen instructions to select the maze difficulty level (easy, medium, or hard) and the search algorithm (BFS, DFS, or A*). The program then displays the solved maze using matplotlib.
## Dependencies
The project relies on several Python libraries for image processing (OpenCV, scikit-image), graph representation (networkx), and visualization (matplotlib).
## Contribution
Contributions to the project are welcome! Users can open issues for bug reports or feature requests, and they can also submit pull requests with improvements or additional features.
## License
The project is licensed under the MIT License, allowing for free use, modification, and distribution, subject to certain conditions. The full license text can be found in the LICENSE file.
