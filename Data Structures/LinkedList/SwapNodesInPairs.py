'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr=head
        prev=dummy
        while curr and curr.next:
            nextPair = curr.next.next
            second=curr.next

            second.next=curr
            curr.next=nextPair
            prev.next=second

            prev=curr
            curr=nextPair
        return dummy.next
