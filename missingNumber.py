def missingNumber_1(nums: List[int]) -> int:        
    """Bitwise sol"""
    n = len(nums)
    res = 0
    for i in range(1,n+1):
        res = res^i
    
    for num in nums:
        res = res ^ num
    
    return res

def missingNumber_2(nums: List[int]) -> int:        
    """Brute solution"""
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
    return -1