'''
You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.

The divisibility array div of word is an integer array of length n such that:

div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
div[i] = 0 otherwise.
Return the divisibility array of word.
'''
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans=[]
        curr=0
        for i in range(len(word)):
            curr=(curr*10+int(word[i]))%m
            if curr==0:
                ans.append(1)
            else:
                ans.append(0)
        return ans
