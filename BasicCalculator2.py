'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''
class Solution:
    def calculate(self, s: str) -> int:
        i=0
        curr=prev=res=0
        currop="+"
        while i<len(s):
            curchar=s[i]
            if curchar.isdigit():
                while i<len(s) and s[i].isdigit():
                    curr=curr*10+int(s[i])
                    i+=1
                i-=1
                if currop=="+":
                    res+=curr
                    prev=curr
                elif currop=="-":
                    res-=curr
                    prev=-curr
                elif currop=="*":
                    res-=prev
                    res+=prev*curr
                    prev=prev*curr
                else:
                    res-=prev
                    res+=int(prev/curr)
                    prev=int(prev/curr)
                curr=0
            elif curchar!=" ":
                currop=curchar
            i+=1
        return res
