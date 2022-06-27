"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
"""


def knapSack(self,W, wt, val, n):
    """Brute Force"""

    if n-1==0 or W == 0:
        return 0

    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)            
    else:
        return max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1), knapSack(W,wt, val, n-1))
            
def knapSack(W, wt, val, n, memo={}):
    """Memoized"""
    if (W, n-1) in memo:
        return memo[(W,n-1)]
    if n-1==0 or W == 0:
        return 0
    if wt[n-1] > W:
        memo[(W,n-1)] = knapSack(W, wt, val, n-1, memo)
        return memo[(W,n-1)]
    else:
        memo[(W,n-1)] = max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1,memo), 
            knapSack(W,wt, val, n-1, memo))
        return memo[(W,n-1)]

def knapSack(W, wt, val, n):
    """Tabulation"""
    dp = [[-1 for _ in range(W+1)] for __ in range(n+1)]

    for i in range(n+1): dp[i][0] = 0
    for i in range(W+1): dp[0][i] = 0


    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]

