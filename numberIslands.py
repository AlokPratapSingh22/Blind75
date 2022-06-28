"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def numberIslands(grid: chr):

    m = len(grid)
    n = len(grid[0])
    vis = [[-1 for _ in range(n)] for __ in range(m)]

    def dfs(i, j):
        row_check = 0 <= i < m
        col_check = 0 <= j < n

        if not row_check or not col_check:
            return

        if vis[i][j] == 1:
            return

        if grid[i][j] == '0':
            return

        vis[i][j] = 1

        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)

    cnt = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and vis[i][j] == -1:
                dfs(i, j)
                cnt += 1

    return cnt
