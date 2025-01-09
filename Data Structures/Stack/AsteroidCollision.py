'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0 and stack[-1]>0:
                if abs(i)>stack[-1]:
                    stack.pop()
                elif abs(i)==stack[-1]:
                    stack.pop()
                    i=0
                else:
                    i=0
            if i:
                stack.append(i)
        return stack
