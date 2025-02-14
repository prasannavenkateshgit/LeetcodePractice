'''
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        ans=0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                ans+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                ans+=maxr-height[r]
        return ans
