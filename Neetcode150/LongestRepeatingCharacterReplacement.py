'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        r=0
        ans=0
        for r in range(len(s)):
            dic[s[r]]+=1
            while (r-l+1)-max(dic.values())>k:
                dic[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
