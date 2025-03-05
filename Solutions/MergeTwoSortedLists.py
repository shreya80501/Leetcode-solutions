# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        head3 = merged = ListNode()

        while( head1 or head2 ):

            if not head1:
                head3.next = head2 #ListNode( head2.val )
                head2 = head2.next
            
            elif not head2:
                head3.next = head1 #ListNode( head1.val )
                head1 = head1.next
            
            else:
                if head1.val <= head2.val:
                    head3.next = head1 #ListNode( head1.val )
                    head1 = head1.next
                else:
                    head3.next = head2 #ListNode( head2.val )
                    head2 = head2.next

            head3 = head3.next

        return merged.next
