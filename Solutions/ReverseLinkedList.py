# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseHelper( self, head ):
        if not head or not head.next:
            return head
        
        front = self.reverseHelper( head.next )
        head.next.next = head
        head.next = None
        return front

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = self.reverseHelper( head )
        return front