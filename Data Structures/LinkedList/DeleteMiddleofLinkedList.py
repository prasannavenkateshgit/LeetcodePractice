'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
'''
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        dummy=ListNode(0,head)
        curr=head
        while curr:
            curr=curr.next
            n+=1
        #n=n-1
        middle = math.floor(n/2)
        print(middle)
        i=0
        start=head
        prev=dummy
        while start:
            if i==middle:
                prev.next=start.next
                return dummy.next
            prev=start
            start=start.next
            i+=1
        #return head

#BETTER SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        dummy=ListNode(0,head)
        prev=dummy
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=prev.next.next
        return dummy.next
