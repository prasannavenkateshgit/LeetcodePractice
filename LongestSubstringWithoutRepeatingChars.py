'''
Given a string s, find the length of the longest substring without duplicate characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        maxlen=0
        l=0
        r=l+1
        maxstr=""
        while r<len(s):
            if s[r] in s[l:r]:
                while l<r and s[l]!=s[r]:
                    l+=1
                l+=1
            #maxlen=max(maxlen,r-l+1)
            if r-l+1>maxlen:
                maxlen=r-l+1
                maxstr=s[l:r+1]
            r+=1
        print(maxstr)
        return maxlen
            
        
