'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        ans=head
        while fast:
            while fast and slow.val == fast.val:
                fast=fast.next
            ans.next=fast
            ans=ans.next
            slow=ans
        return head
