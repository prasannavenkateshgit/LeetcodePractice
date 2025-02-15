'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=set()
        maxlen=0
        l=0
        r=0
        while r<len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            sub.add(s[r])
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
