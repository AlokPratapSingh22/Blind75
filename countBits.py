"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""

def countBits_1(n:int)->list[int]:
    """bitwise solution"""
    if n==0:
        return [0]
    dp = [0,1]
    
    for i in range(2,n+1):
        cnt = 0
        while i != 0:
            cnt+=1
            i &= (i-1)
        dp.append(cnt)
    return dp

def countBits(self, n: int) -> List[int]:
    if n==0:
        return [0]
    dp = [0,1]
    
    for i in range(2,n+1):
        if i%2 == 0:
            dp.append(dp[i//2])
        else:
            dp.append(1+dp[i//2])
    return dp