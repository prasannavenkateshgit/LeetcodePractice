'''
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
'''
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans=0
        i=0
        left=0
        cost=0
        while i<len(s):
            cost+=abs(ord(s[i])-ord(t[i]))
            while cost>maxCost:
                cost=cost-abs(ord(s[left])-ord(t[left]))
                left+=1
            ans=max(ans,len(s[left:i+1]))
            i+=1
        return ans
