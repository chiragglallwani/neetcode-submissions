class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            print(ops)
            if ops == "+":
                element1 = stack[-1]
                element2 = stack[-2]
                res = element1 + element2
                stack.append(res)
            elif ops == "D":
                element1 = stack[-1]
                res = element1 * 2
                stack.append(res)
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
            print(stack)
        print(stack)
        result = sum(stack)
        return result
                