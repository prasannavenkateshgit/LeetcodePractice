'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        iterations=min(len(s),len(t))
        for i in range(iterations):
            if s[i] == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
            if t[i] == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[i])
        if iterations<len(s):
            j=iterations
            while j<len(s):
                if s[j]=="#":
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(s[j])
                j+=1
        if iterations<len(t):
            k=iterations
            while k<len(t):
                if t[k]=="#":
                    if stack2:
                        stack2.pop()
                else:
                    stack2.append(t[k])
                k+=1
        return "".join(stack1)=="".join(stack2)
                
        
