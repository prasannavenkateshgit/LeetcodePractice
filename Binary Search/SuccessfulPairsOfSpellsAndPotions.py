'''
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        potions.sort()
        for i in spells:
            target=success/i
            left=0
            right=len(potions)
            while left<right:
                mid=(left+right)//2
                if potions[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            ans.append(len(potions)-left)
        return ans
