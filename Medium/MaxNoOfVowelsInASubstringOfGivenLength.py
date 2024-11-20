'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        substr=''
        i=0
        maxvowels=0
        currcount=0
        vowels=['a','e','i','o','u']
        while i<len(s):
            substr+=s[i]
            if s[i] in vowels:
                currcount+=1
            #maxvowels = max(maxvowels,currcount)
            while len(substr)>k:
                if substr[0] in vowels:
                    currcount-=1
                #maxvowels = max(maxvowels,currcount)
                substr=substr[1:]
            maxvowels = max(maxvowels,currcount)
            i+=1
        # maxvowels2=0
        # if len(s)==k:
        #     for i in s:
        #         if i in vowels:
        #             maxvowels2+=1
        #     return maxvowels2
        return maxvowels
