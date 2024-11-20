'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        maps={}
        for i in range(len(s)):
            if s[i] in maps:
                if maps[s[i]]!=t[i]:
                    return False
            else:
                maps[s[i]]=t[i]
        maps2={}
        for j in range(len(t)):
            if t[j] in maps2:
                if maps2[t[j]]!=s[j]:
                    return False
            else:
                maps2[t[j]]=s[j]
        return True
