# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        startNode = ListNode()
        tail = startNode
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 # Remember list1 is just a node with next address not a list
                list1 = list1.next
            else:
                tail.next = list2 # Remember list2 is just a node with next address not a list
                list2 = list2.next
            tail = tail.next # We did this next because we need to increment the pointer
        tail.next = list1 if list1 else list2
        return startNode.next