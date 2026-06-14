from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        size = len(self.queue)
        self.queue.append(x)

        for _ in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty stack")
        print(self.queue)
        return self.queue.popleft()

    def top(self) -> int:
        print(self.queue)
        return self.queue[0]

    def empty(self) -> bool:
        print(self.queue)
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()