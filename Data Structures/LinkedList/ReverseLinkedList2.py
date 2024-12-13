'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftprev,curr=dummy,head
        for i in range(left-1):
            leftprev=curr
            curr=curr.next
        prev=None
        for i in range(right-left+1):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        leftprev.next.next = curr
        leftprev.next=prev
        
        return dummy.next
