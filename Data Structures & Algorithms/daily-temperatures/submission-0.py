class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair (temp, index)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #curr_temp > last stored temp in stack
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return result