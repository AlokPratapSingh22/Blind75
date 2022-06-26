"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


def search(nums: List[int], target: int) -> int:
    """
    Correct  O(log N) solution
    """
    l,r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid+1
            else:
                r = mid-1
    return -1

def search_2(nums:list[int], target: int) -> int:
    """
        My own devised logic
    """
    # Find the rotation point
    def findMin(nums: List[int]) -> int:
        
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
    # Binary Search
    def binarySearch(l,r, target):
        if l > r:
            return -1
        mid = (l+r)//2

        if target == nums[mid]:
            return mid
        
        if nums[mid] > target:
            return binarySearch(l, mid-1, target)
        else:
            return binarySearch(mid+1, r, target)
    
    pt = findMin(nums)

    l = binarySearch(0, pt, target)
    r = binarySearch(pt, len(nums)-1, target)

    return max(l, r)
