"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""

def findMin(nums: list[int]) -> int:
    """
    Brute force
    
    O(N) method
    """        
    if nums[-1] >= nums[0]:
        return nums[0]
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return nums[i+1]
    return nums[0]

def findMin_binary_search(nums: List[int]) -> int:
    """O(log N) method"""    
    l,r = 0, len(nums)-1
    if nums[l] <= nums[r]:return nums[0]
    
    while l<r:
        mid = (l+r)//2
        
        if nums[l] < nums[mid]:
            l = mid+1
        elif nums[mid] < nums[l]:
            r = mid-1
            
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        
            
    return nums[0]