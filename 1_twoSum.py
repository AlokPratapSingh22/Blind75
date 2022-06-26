"""
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
"""

def brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return (i, j)
    return (-1, -1)

def optimized_1(nums:list[int], target: int) -> list[int]:
    num_dict = {num:i for i,num in enumerate(nums)}

    for i in range(len(nums)):
        num = nums[i]
        if target-num in num_dict:
            if i != num_dict[target-num]:
                return (i,num_dict[target-num])

    return (-1,-1)

def optimized_2(nums:list[int], target:int) -> list[int]:
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort()
    
    i = 0
    j = len(arr)-1
    
    while i < j:
        s = arr[i][0]+arr[j][0]
        if s < target:
            i+=1
        elif s > target:
            j-=1
        else:
            return (arr[i][1],arr[j][1])
    return (-1,-1)
    
print(brute_force([2, 7, 11, 5], 9))
print(optimized_1([2,7,11,5], 9))
print(optimized_2([2,7,11,5], 9))
