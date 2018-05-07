# Insert Interval
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
# 
# Example 1:
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        head, mid, tail = search(intervals, start, end)
        mid = merge(mid, start, end)
        return head+mid+tail

def search(intervals, start, end):
    head = []
    mid = []
    tail = []
    for obj in intervals:
        if obj.end < start:
            head.append(obj)
            continue
        if obj.start > end:
            tail.append(obj)
            continue
        mid.append(obj)
    return head, mid, tail

def merge(mid, start, end):
    if len(mid) == 0:
        return [Interval(start, end)]
    s = min(mid[0].start, start)
    e = max(mid[-1].end, end)
    intval = Interval(s, e)
    return [intval]


