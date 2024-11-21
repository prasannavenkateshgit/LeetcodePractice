'''
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1=defaultdict(int)
        left=0
        right=len(s1)
        for i in s1:
            counts1[i]+=1
        while right <=len(s2):
            test=s2[left:right]
            counts2=defaultdict(int)
            for j in test:
                counts2[j]+=1
            found=0
            for k in counts1:
                if counts1[k]==counts2[k]:
                    found+=1
            if found==len(set(s1)):
                return True
            left+=1
            right+=1
        return False
