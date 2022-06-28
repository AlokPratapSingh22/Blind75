"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    print(nums)
    cnt = 1
    max_cnt = 0
    for i in range(len(nums)):
        if i+1<len(nums) and nums[i] == nums[i+1]:
            continue
        if i+1<len(nums) and nums[i]+1 == nums[i+1]:
            cnt+=1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            
    return max_cnt