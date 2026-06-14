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
        # closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        # for char in s:
        #     if char in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[char]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)
        
        # return True if not stack else False
        if len(s) % 2 != 0:
            return False
        stack = []
        for bracket in s:
            if bracket == '}':
                if not self.hasOpeningParenthesesInStack(stack, '{'):
                    return False
            elif bracket == ')':
                if not self.hasOpeningParenthesesInStack(stack, '('):
                    return False
            elif bracket == ']':
                if not self.hasOpeningParenthesesInStack(stack, '['):
                    return False
            else:
                stack.append(bracket)
        return True if len(stack) == 0 else False
