'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nos={}
        dummy = ListNode(0,head)
        prev=dummy
        curr=head
        while curr:
            if curr.val in nos:
                prev.next = curr.next
                nos[curr.val]+=1
            else:
                nos[curr.val]=1
            prev=curr
            curr=curr.next
        start=dummy.next
        newprev=dummy
        print(nos)
        while start:
            if nos[start.val]>1:
                newprev.next=start.next
                start=start.next
            else:
                newprev=start
                start=start.next
        return dummy.next
