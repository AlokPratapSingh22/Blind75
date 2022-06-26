"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

def productArray(nums:list[int]):
    total_product = 1
    cntZero = 0
    for num in nums: 
        total_product*=num
        if num == 0:
            cntZero+=1

    if total_product !=0:
        return [total_product//num for num in nums]
    if cntZero > 1:
        return [0]*len(nums)

    prod = []
    for i in range(len(nums)):
        if nums[i] == 0:
            p = 1
            for j in range(0, len(nums)):
                if i != j:
                    p*=nums[j]

            prod.append(p)
        else:
            prod.append(0)
    return prod