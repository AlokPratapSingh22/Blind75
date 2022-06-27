"""
iven an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0
"""

def combinationSum(self, nums: List[int], target: int) -> int:
    """bruteforce"""
    def helper(target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        cnt = 0
        for num in nums:
            if target - num >= 0:
                cnt += helper(target-num)

        return cnt
    return helper(target)


def combinationSum(self, nums: List[int], target: int) -> int:
    """Memoized"""
    def helper(target, memo={}):
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        cnt = 0
        for num in nums:
            if target - num >= 0:
                cnt += helper(target-num, memo)
        memo[target] = cnt
        return cnt
    return helper(target)


def combinationSum4(self, nums: List[int], target: int) -> int:
    """Tabulation"""
    dp = [0 for _ in range(target+1)]
    dp[0] = 1

    for i in range(target+1):
        if dp[i] == 0:
            continue
        for num in nums:
            if i+num <= target:
                dp[i+num] += dp[i]
    return dp[target]
