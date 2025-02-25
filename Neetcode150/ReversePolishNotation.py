'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                temp1=stack.pop()
                temp2=stack.pop()
                if i=="+":
                    stack.append(temp2+temp1)
                elif i=="-":
                    stack.append(temp2-temp1)
                elif i=="*":
                    stack.append(temp2*temp1)
                else:
                    stack.append(int(temp2/temp1))
                print(stack)
            else:
                stack.append(int(i))
        return stack[-1]
