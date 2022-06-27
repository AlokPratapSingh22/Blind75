"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


def rob(nums: List[int]) -> int:
    """Bruteforce"""
    def helper(i, s):
        if i >= len(nums):
            return s

        return max(helper(i+2, s+nums[i]), helper(i+1, s))
    return helper(0, 0)


def rob(nums: List[int]) -> int:
    """Memoized"""
    def helper(i, s, memo={}):
        if (s, i) in memo:
            return memo[(s, i)]
        if i >= len(nums):
            memo[(s, i)] = s
            return s

        memo[(s, i)] = max(helper(i+2, s+nums[i], memo), helper(i+1, s, memo))
        return memo[(s, i)]
    return helper(0, 0)


def rob(nums: List[int]) -> int:
    """Tabulation"""
    if len(nums) == 0:
        return 0
    dp = [0 for _ in range(len(nums)+1)]
    dp[0] = 0
    dp[1] = nums[0]
    for i in range(1, len(nums)):
        dp[i+1] = max(dp[i-1]+nums[i], dp[i])

    return dp[len(nums)]


def rob(nums: List[int]) -> int:
    """Optimized"""
    incl = 0
    excl = 0
    for num in nums:
        n_excl = max(excl, incl)
        incl = excl + num
        excl = n_excl

    return max(incl, excl)
