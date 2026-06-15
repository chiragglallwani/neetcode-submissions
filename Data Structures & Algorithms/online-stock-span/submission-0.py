class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 0
        reverseIndex = -1
        while abs(reverseIndex) <= len(self.stack) and self.stack[reverseIndex] <= price:
            count += 1
            reverseIndex -= 1
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)