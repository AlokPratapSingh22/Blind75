"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = set()
    for k in range(len(nums)):
        i,j = k+1, len(nums)-1
        while i < j:
            if nums[i]+nums[j] == -nums[k]:
                ans.add((nums[k],nums[i],nums[j]))
                i+=1
            elif nums[i]+nums[j] > -nums[k]:
                j-=1
            else:
                i+=1
        
    return list(ans)

def threeSum_better(nums:list[int])->list[list[int]]:
    nums.sort()
    if len(nums) == 0 or nums[0]>0:
        return []        
    ans = []
    for k in range(len(nums)-2):
        if k == 0 or nums[k]!=nums[k-1]:
            i,j = k+1, len(nums)-1            
            while i < j:
                if nums[i]+nums[j] == -nums[k]:
                    ans.append((nums[k],nums[i],nums[j]))
                    while (i < j and nums[i] == nums[i+1]): i+=1
                    while (i < j and nums[j] == nums[j-1]): j-=1
                    i+=1
                    j-=1
                elif nums[i]+nums[j] > -nums[k]:
                    j-=1
                else:
                    i+=1
        
    return ans
