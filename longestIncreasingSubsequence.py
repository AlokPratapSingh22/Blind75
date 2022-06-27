"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
import bisect

def lengthOfLIS(nums: List[int]) -> int:
    """Bruteforce"""
    def helper(i, prev):            
        
        if i >= len(nums)-1:
            return 0
        
        excl = helper(i+1, prev)
        
        incl = 0
        if nums[i] > prev:
            incl = 1 + helper(i+1, nums[i])            
        
        return max(incl, excl)
    
    return helper(0, -math.inf)


def lengthOfLIS(nums: List[int]) -> int:
    """Memoized"""
    def helper(i, prev, memo = {}):            
        if (i, prev) in memo:
            return memo[(i, prev)]
        if i >= len(nums):
            return 0
        
        excl = helper(i+1, prev, memo)
        
        incl = 0
        if nums[i] > prev:
            incl = 1 + helper(i+1, nums[i], memo)            
        
        memo[(i, prev)] = max(incl, excl)
        return memo[(i, prev)]
    
    return helper(0, -math.inf)

def lengthOfLIS(nums: List[int]) -> int:
    """Tabulation"""
    if not nums: return 0

    n = len(nums)
    ar = [0]*n
    ar[0] = 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and ar[j]> ar[i]:
                ar[i] = ar[j]
        ar[i] += 1

    return max(ar)


def lengthOfLIS(self, nums: List[int]) -> int:
    """Max optimized"""
    result = []
    
    for num in nums:
        #get the index where we can add this num in result array using binary search module
        i = bisect.bisect_left(result,num)
        
        #if this num is greater than all numbers in result array add this to the end
        if i == len(result):
            result.append(num)
        #otherwise replace the number at the index in result
        elif result[i] > num:
            result[i] = num
    #the length of the array gives the longest increasing subsequence of nums        
    return len(result)
