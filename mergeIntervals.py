"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
        Blindly Sorting
        O(nlogn) time complexity and O(1) space complexity
    """
    intervals.sort()
    j = len(intervals) -1
    i = 0 
    while i < j:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            intervals.pop(i+1)
            i-=1
            j-=1
        i+=1
    
    return intervals

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    """
        Sorting and inserting values accordingly
        O(nlogn) time and O(n) space
    """
    intervals.sort()
    
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged