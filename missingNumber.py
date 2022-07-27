def missingNumber_1(nums: List[int]) -> int:        
    """Bitwise sol"""
    n = len(nums)
    res = 0
    for i in range(1,n+1):
        res = res^i
    
    for num in nums:
        res = res ^ num
    
    return res

# USING SUM(RANGE) - SUM(ARRAY)
def missingNumber_3(self, nums: List[int]) -> int:        
        r = len(nums)
               
        for i, n in enumerate(nums): r += (i-n)
            
        return r

def missingNumber_2(nums: List[int]) -> int:        
    """Brute solution"""
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
    return -1
