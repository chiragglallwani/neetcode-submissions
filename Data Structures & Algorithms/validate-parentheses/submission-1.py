class Solution:
    def isStackEmpty(self, stack: list) -> bool:
        return len(stack) == 0 if True else False
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if self.isStackEmpty(stack):
                    return False
                last_item = stack[-1]
                if last_item != '(':
                    return False
                else:
                    stack.pop()
            elif char == '}':
                if self.isStackEmpty(stack):
                    return False
                last_item = stack[-1]
                if last_item != '{':
                    return False
                else:
                    stack.pop()
            elif char == ']':
                if self.isStackEmpty(stack):
                    return False
                last_item = stack[-1]
                if last_item != '[':
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0 if True else False