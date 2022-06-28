"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(nums: List[int]) -> bool:
    """Bruteforce"""
    def helper(i):
        if i == len(nums)-1:
            return True

        if i >= len(nums) or nums[i] == 0:
            return False

        for j in range(1, nums[i]+1):
            if helper(i+j):
                return True
        return False
    return helper(0)


def canJump(nums: List[int]) -> bool:
    """Memoized"""
    def helper(i, memo={}):
        if i in memo:
            return memo[i]
        if i == len(nums)-1:
            return True

        if i >= len(nums) or nums[i] == 0:
            return False

        for j in range(nums[i], 0, -1):
            if helper(i+j, memo):
                memo[i] = True
                return True
        memo[i] = False
        return False
    return helper(0)


def canJump(nums: List[int]) -> bool:
    """Tabulation"""
    dp = [False]*(len(nums)+1)
    dp[0] = True

    for i in range(len(nums)):
        if not dp[i]:
            continue
        for j in range(1, nums[i]+1):
            if i+j < len(nums)+1:
                dp[i+j] = True
    return dp[len(nums)]


def canJump(nums: List[int]) -> bool:
    """Optimized"""
    last = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= last:
            last = i
    return last <= 0
