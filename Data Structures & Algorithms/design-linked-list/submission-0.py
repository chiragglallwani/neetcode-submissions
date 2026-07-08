class ListNode:
    def __init__(self, val = -1, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # self.head should be dummy node & should never be modified
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0


    def get(self, index: int) -> int:
        count = 0
        curr = self.head.next
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode # never destroy the reference.

        # if tail is same head previously
        if not newNode.next:
            self.tail = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
      self.tail.next = ListNode(val)
      self.tail = self.tail.next
      self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = ListNode(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)