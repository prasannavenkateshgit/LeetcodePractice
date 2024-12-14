'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        l=0
        while curr:
            curr=curr.next
            l+=1
        remove=l-n+1
        print(remove)
        i=0
        start=head
        while start:
            i+=1
            if i==remove:
                prev.next=start.next
                return dummy.next
            prev=start
            start=start.next
