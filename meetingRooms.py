"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
(0,8),(8,10) is not conflict at 8

Examples

Example1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

Example2:
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: Two times will not conflict 
"""


def can_attend_meetings(intervals: List[Interval]) -> bool:
    """Simple"""
    minm = -math.inf
    for interval in sorted(intervals, key=lambda x: x.end):
        if minm != -math.inf and minm > interval.start:
            return False
        else:
            minm = interval.end
    return True
