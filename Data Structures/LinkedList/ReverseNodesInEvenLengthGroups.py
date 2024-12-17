'''
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        node = None
        reverse = None
        currNext = None
        curr = None
        prevNext = None
        groupLen = 2
        numNodes = 0
        while(prev.next != None):
            node=prev
            numNodes=0
            i=0
            for i in range(groupLen):
                if (node.next == None):
                    break
                numNodes+=1
                node=node.next
            
            if(numNodes%2 !=0):
                prev=node
            else:
                reverse=node.next
                curr=prev.next
                j=0
                for j in range(numNodes):
                    currNext = curr.next
                    curr.next = reverse
                    reverse = curr
                    curr = currNext
                
                prevNext = prev.next
                prev.next = node
                prev = prevNext
            groupLen+=1
        return head
        
