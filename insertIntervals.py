from typing import List
"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """O(N) time and O(1) space can be achieved"""
    index = -1
    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[0]:
            index = i
            break
    if index == -1:
        intervals.append(newInterval)
    else:
        intervals.insert(index, newInterval)   
    
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            merged[-1][0] = min(merged[-1][0], interval[0])

    return merged

def insert(intervals: List[List[int]], newInterval: List[int]):
    """
        Better
        O(logN) time and O(1) space
    """
    def findPivot(start, end, target):
        while start <= end:
            mid = (start + end) // 2

            if intervals[mid][0] <= target <= intervals[mid][1]:
                return mid
            
            elif target > intervals[mid][0]:
                start = mid + 1
            else:
                end = mid - 1
        return start

    n = len(intervals)

    start_pivot = findPivot(0, n-1, newInterval[0])
    if start_pivot < n and intervals[start_pivot][0] <= newInterval[0] <= intervals[start_pivot][1]:
        newInterval[0] = intervals[start_pivot][0]
        newInterval[1] = max(intervals[start_pivot][1], newInterval[1])
    
    end_pivot = findPivot(0, n-1, newInterval[1])
    if end_pivot < n and intervals[end_pivot][0] <= newInterval[1] <= intervals[end_pivot][1]:
        newInterval[1] = intervals[end_pivot][1]
        end_pivot+=1
    
    intervals[start_pivot:end_pivot] = [newInterval]
    return intervals
