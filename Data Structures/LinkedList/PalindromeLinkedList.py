'''
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(0,head)
        prev=None
        curr=head
        start=head
        left=[]
        while start:
            left.append(start.val)
            start=start.next
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        rev=prev
        right=[]
        while rev:
            right.append(rev.val)
            rev=rev.next
        if left==right:
            return True
        else:
            return False
