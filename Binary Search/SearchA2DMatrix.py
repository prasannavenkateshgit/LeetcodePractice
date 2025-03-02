'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # oned=[]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         oned.append(matrix[i][j])
        # left=0
        # right=len(oned)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if oned[mid]==target:
        #         return True
        #     elif oned[mid]>target:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # return False
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            num=matrix[row][col]
            if num==target:
                return True
            elif num>target:
                right=mid-1
            else:
                left=mid+1
        return False
