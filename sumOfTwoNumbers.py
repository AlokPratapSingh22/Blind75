"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

nums and res in 32-bit int.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
"""

def getSum(a: int, b: int) -> int:
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    
    mask = 0xFFFFFFFF
    
    while b!=0:            
        a, b = (a ^ b) & mask, ((a&b) << 1)&mask
        
        
    return a if a<= MAX else ~(a^mask)    