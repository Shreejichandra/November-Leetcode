'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = [0,0]
        n = len(intervals)
        ans = []
        if n == 0:
            return ans
        intervals.sort()
        new[0] = intervals[0][0]
        new[1] = intervals[0][1]
        
        
        for j in range(1, n):
            if new[1] < intervals[j][0]:
                ans.append([new[0], new[1]])
                new[0] = intervals[j][0]
                new[1] = intervals[j][1]
                
            else:
                new[0] = min(new[0], intervals[j][0])
                new[1] = max(new[1], intervals[j][1])
        ans.append([new[0], new[1]])
        return ans
        
