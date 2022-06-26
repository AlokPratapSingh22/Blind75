"""
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.

    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums: List[int]) -> int:
    max_sum = 0
    curr_sum = 0
    mx = -math.inf
    
    for num in nums:
        mx = max(num, mx)            
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
        
        if curr_sum < 0:                
            curr_sum = 0
        
    
    return max_sum if max_sum > 0 else mx