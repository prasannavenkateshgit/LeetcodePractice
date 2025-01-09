'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''
import collections
class MinStack:

    def __init__(self):
        self.stack = []
        self.que = collections.deque()
        

    def push(self, val: int) -> None:
        self.que.append(val)
        if val<=self.que[0]:
            self.que.appendleft(val)

        

    def pop(self) -> None:
        temp=self.que.pop()
        if temp==self.que[0]:
            self.que.popleft()

        

    def top(self) -> int:
        return self.que[-1]
        

    def getMin(self) -> int:
        return self.que[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
