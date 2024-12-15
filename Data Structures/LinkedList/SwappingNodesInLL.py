'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        n=1
        start=head
        while start:
            start=start.next
            n+=1
        print(n)
        curr=head
        i=1
        prev=dummy
        leftprev=None
        leftcurr=None
        leftnext=None
        rightprev=None
        rightcurr=None
        rightnext=None
        while curr:
            if i == k:
                leftprev=prev
                leftcurr=curr
                leftnext=curr.next
            if i == n-k:
                rightprev=prev
                rightcurr=curr
                rightnext=curr.next
            prev=curr
            curr=curr.next
            i+=1
        tmp=leftcurr.val
        leftcurr.val=rightcurr.val
        rightcurr.val=tmp
        return dummy.next
