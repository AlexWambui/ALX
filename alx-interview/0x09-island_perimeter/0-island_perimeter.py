#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island on a grid.

    Args:
        grid (list[list[int]]): A 2D grid representing land and water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    if not isinstance(grid, list):
        return 0

    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 0:
                continue

            edges = (
                i == 0 or grid[i - 1][j] == 0,  # Above
                j == cols - 1 or grid[i][j + 1] == 0,  # Right
                i == rows - 1 or grid[i + 1][j] == 0,  # Below
                j == 0 or grid[i][j - 1] == 0  # Left
            )

            perimeter += sum(edges)
    return perimeter
