class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # for token in tokens:
        #     if token == '+':
        #         stack.append(stack.pop() + stack.pop())
        #     elif token == "-":
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(b - a)
        #     elif token == "*":
        #         stack.append(stack.pop() * stack.pop())
        #     elif token == "/":
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(int(float(b) / a))
        #     else:
        #         stack.append(int(token))
        # return stack[0]
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                ele1 = stack.pop()
                ele2 = stack.pop()
                if token == "+":
                    stack.append(ele2 + ele1)
                elif token == "-":
                    stack.append(ele2 - ele1)
                elif token == "*":
                    stack.append(ele2 * ele1)
                elif token == "/":
                    stack.append(int(ele2 / ele1))
            else:
                stack.append(int(token))
        return stack[0]