# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Approach: 
        Step 1: Find the mid of the linked list,
        Step 2: Break into two linked list
        Step 3: Reverse the second half of linked list
        Step 4: Merge two linked list alternatively
        """

        # Step 1
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  

        # Step 2
        prev, curr = None, slow.next
        slow.next = None
        
        # Step 3
        while curr:
            nxt = curr.next  # Attach rest of nodes to new linked list
            curr.next = prev # Attach all previous nodes to current node.
            prev = curr      # Increase the point or say prev node is now the current node (all nodes in previous are now reverse linked)
            curr = nxt       # Increase the curr pointer or rest of old nodes are set as curr  

        # Step 4
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


