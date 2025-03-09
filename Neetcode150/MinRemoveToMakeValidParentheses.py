'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=[]
        cnt=0
        for i in s:
            if i=="(":
                res.append(i)
                cnt+=1
            elif i==")" and cnt>0:
                cnt-=1
                res.append(i)
            elif i!=")":
                res.append(i)
        ans=[]
        for i in res[::-1]:
            if i=="(" and cnt>0:
                cnt-=1
            else:
                ans.append(i)
        return "".join(ans[::-1])
