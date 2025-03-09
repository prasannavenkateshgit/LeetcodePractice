'''
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ans=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                ans = max(ans, height*(i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            ans=max(ans, h*(len(heights)-i))
        return ans
