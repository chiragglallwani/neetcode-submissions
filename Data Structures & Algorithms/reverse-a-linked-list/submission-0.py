# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:  3 Pointer approach with prev, curr, next.
        Store the curr.next node in next, set curr.next = prev
        prev = curr, next = curr while curr is not null
        """

        prev, curr = None, head

        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev