"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""


def rob(nums: List[int]) -> int:
    """Bruteforce"""
    def helper(i, s, first):
        if i >= len(nums):
            return s
        if first and i == len(nums)-1:
            return s
        return max(helper(i+2, s+nums[i], first), helper(i+1, s, first))
    return max(helper(1, 0, False), helper(2, nums[0], True))


def rob(nums: List[int]) -> int:
    """Memoized"""
    def helper(i, s, first, memo={}):
        if (i, s) in memo:
            return memo[(i, s)]
        if i >= len(nums):
            memo[(i, s)] = s
            return s
        if first and i == len(nums)-1:
            memo[(i, s)] = s
            return s
        memo[(i, s)] = max(helper(i+2, s+nums[i], first, memo),
                           helper(i+1, s, first, memo))
        return memo[(i, s)]

    return max(helper(1, 0, False, {(0, 0): 0}), helper(2, nums[0], True))


def rob(arr: List[int]) -> int:
    """Tabulation"""
    def helper(nums):
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i-1]+nums[i], dp[i])

        return dp[len(nums)]

    if len(arr) == 1:
        return arr[0]

    return max(helper(arr[1:]), helper(arr[:-1]))


def rob(arr: List[int]) -> int:
    """Optimized"""
    def helper(nums):
        incl = 0
        excl = 0
        for num in nums:
            n_excl = max(excl, incl)
            incl = excl + num
            excl = n_excl

        return max(incl, excl)

    if len(arr) == 1:
        return arr[0]

    return max(helper(arr[1:]), helper(arr[:-1]))
