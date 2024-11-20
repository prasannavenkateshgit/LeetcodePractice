'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def checkPalindrome(s):
            i=0
            j=len(s)-1
            ispali=True
            while i<j:
                if s[i]!=s[j]:
                    ispali=False
                i=i+1
                j=j-1
            return ispali

        if len(palindrome)==1:
            return ""
        else:
            i=0
            while i<int(len(palindrome)/2):
                if palindrome[i]!='a':
                    temp=palindrome
                    palindrome=list(palindrome)
                    palindrome[i]='a'
                    palindrome="".join(palindrome)
                    if checkPalindrome(palindrome):
                        palindrome=temp
                    else:
                        return palindrome
                i=i+1
            palindrome=list(palindrome)
            palindrome[-1]='b'
            palindrome="".join(palindrome)
            return palindrome
