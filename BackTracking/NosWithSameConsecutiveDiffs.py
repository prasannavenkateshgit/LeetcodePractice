'''
Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        ans=[]
        def dfs(N, num):
            if N == 0:
                return ans.append(num)
            tail=num%10
            nextdigits=set([tail+k, tail-k])
            for nextd in nextdigits:
                if 0<=nextd<10:
                    newnum=num*10+nextd
                    dfs(N-1,newnum)
        for num in range(1,10):
            dfs(n-1,num)
        return list(ans)
        
