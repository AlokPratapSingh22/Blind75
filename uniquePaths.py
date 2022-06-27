"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


def uniquePaths(m: int, n: int) -> int:
    """Bruteforce"""
    def get_total_paths(i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        if j == n-1 and i == m-1:
            return 1

        return get_total_paths(i+1, j) + get_total_paths(i, j+1)

    return get_total_paths(0, 0)


def uniquePaths(m: int, n: int) -> int:
    """Memoization"""
    def get_total_paths(i, j, memo={}):
        if (i, j) in memo:
            return memo[(i, j)]
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0

        if j == n-1 and i == m-1:
            return 1

        memo[(i, j)] = get_total_paths(i+1, j, memo) + \
            get_total_paths(i, j+1, memo)
        return memo[(i, j)]

    return get_total_paths(0, 0)


def uniquePaths(self, m: int, n: int) -> int:
    """Tabulation"""
    dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
    dp[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i+1 <= m:
                dp[i+1][j] += dp[i][j]
            if j+1 <= n:
                dp[i][j+1] += dp[i][j]
    return dp[m][n]
