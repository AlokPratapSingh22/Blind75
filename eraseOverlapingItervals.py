"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """Jumping into it
       O(N logN) time and constant space
    """
    intervals.sort(key=lambda x: x[1])
    cnt = 0
    last = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] < last:
            cnt += 1
        else:
            last = interval[1]

    return cnt


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """Optimized"""
    cnt = 0
    last = -math.inf
    for x, y in sorted(intervals, key=lambda i: i[1]):
        if x < last:
            cnt += 1
        else:
            last = y

    return cnt
