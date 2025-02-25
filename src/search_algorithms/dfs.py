import pygame
from maze_generator import highlight_cell, get_neighbors_coord, reconstruct_path, DELAY, BLUE, ORANGE, PURPLE, GREEN

def solve_dfs(maze, win):
    """
    Solve the maze using Depth-First Search (DFS) and animate the search.
    The search starts at the top-left cell (0,0) and ends at the bottom-right cell.
    """
    start = (0, 0)
    end = (maze.rows - 1, maze.cols - 1)
    stack = [start]
    came_from = {start: None}
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)

        # Visualize the current state of the search
        maze.draw(win)
        for cell in visited:
            highlight_cell(win, cell, BLUE, maze.cell_size)
        for cell in stack:
            highlight_cell(win, cell, ORANGE, maze.cell_size)
        highlight_cell(win, current, PURPLE, maze.cell_size)
        pygame.display.update()
        pygame.time.delay(DELAY)

        if current == end:
            break

        for neighbor in get_neighbors_coord(current, maze):
            if neighbor not in visited and neighbor not in stack:
                came_from[neighbor] = current
                stack.append(neighbor)

    # Reconstruct and animate the final solution path
    path = reconstruct_path(came_from, start, end)
    for cell in path:
        maze.draw(win)
        for path_cell in path:
            highlight_cell(win, path_cell, GREEN, maze.cell_size)
        pygame.display.update()
        pygame.time.delay(DELAY)