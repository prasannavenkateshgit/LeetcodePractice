'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return (skipl==skipl[::-1] or skipr==skipr[::-1])
            l+=1
            r-=1
        return True
