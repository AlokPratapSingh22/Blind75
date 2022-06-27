"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

def climbStairs(n: int) -> int:
    """Fibonacci"""
    if n==0:
        return 0
    if n == 1:
        return 1
    if n==2:
        return 2
    
    a = 1
    b = 2
    for i in range(3, n+1):            
        t = a
        a = b
        b = t+b            
        
    return 
