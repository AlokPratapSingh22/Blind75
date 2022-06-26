"""217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
"""

def containsDuplicate_1(nums: List[int]) -> bool:        
    """using sets"""
    l = len(nums)
    nums = set(nums)        

    if l != len(nums):
        return True

    return False

def containsDuplicate_2(nums: list[int]) -> bool:
    """simple traversal over sorted array"""
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False

