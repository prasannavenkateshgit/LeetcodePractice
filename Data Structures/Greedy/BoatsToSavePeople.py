'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans=0
        i=0
        j=len(people)-1
        people.sort()
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            ans+=1
        return ans
