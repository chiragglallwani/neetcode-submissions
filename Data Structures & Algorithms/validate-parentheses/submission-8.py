class Solution:
    def hasOpeningParenthesesInStack(self, stack: list, target: str) -> bool:
        if len(stack) == 0:
            return False
        if stack.pop() != target:
            return False
        return True
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        # stack = []
        # for bracket in s:
        #     if bracket == '}':
        #         if not self.hasOpeningParenthesesInStack(stack, '{'):
        #             return False
        #     elif bracket == ')':
        #         if not self.hasOpeningParenthesesInStack(stack, '('):
        #             return False
        #     elif bracket == ']':
        #         if not self.hasOpeningParenthesesInStack(stack, '['):
        #             return False
        #     else:
        #         stack.append(bracket)
        # return True if len(stack) == 0 else False
        if len(s) % 2 != 0:
            return False
        match = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in match:
                if not stack or stack[-1] != match[bracket]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)
        return len(stack) == 0


