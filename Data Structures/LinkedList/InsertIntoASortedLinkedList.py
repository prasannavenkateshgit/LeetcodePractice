'''
Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            temp=Node(insertVal)
            temp.next=temp
            return temp
        curr=head
        while curr.next!=head:
            if curr.val<=insertVal<=curr.next.val:
                temp=Node(insertVal,curr.next)
                curr.next=temp
                return head
            elif curr.val>curr.next.val:
                if insertVal>=curr.val or insertVal<=curr.next.val:
                    temp=Node(insertVal,curr.next)
                    curr.next=temp
                    return head
            curr=curr.next
        temp=Node(insertVal,curr.next)
        curr.next=temp
        return head
