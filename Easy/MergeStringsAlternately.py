'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

#Runtime 26ms, beats 96.7% of users with Python3
#Space 16.6 MB, beats 53.3% of users with Python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<len(word2):
            smallerlen=len(word1)
        else:
            smallerlen=len(word2)
        i=0
        newstr=['']*(len(word1)+len(word2))
        j=0
        print(smallerlen)
        print(word1[0])
        while j<smallerlen:
            newstr[i]=word1[j]
            newstr[i+1]=word2[j]
            i=i+2
            j=j+1
        if len(word1)>smallerlen:
            newstr.append(word1[smallerlen:])
        elif len(word2)>smallerlen:
            newstr.append(word2[smallerlen:])
        return ''.join(newstr)
        
