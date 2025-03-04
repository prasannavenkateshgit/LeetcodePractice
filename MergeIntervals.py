'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0]<=ans[-1][1] and intervals[i][1]<=ans[-1][1]:
                continue
            if intervals[i][0]<=ans[-1][1]:
                a=ans.pop()
                b=intervals[i][1]
                ans.append([a[0],b])
            else:
                ans.append(intervals[i])
        return ans
        
