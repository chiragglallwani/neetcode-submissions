class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        chars = ""
        nums = 0
        for char in s:
            if char.isdigit():
                nums = nums*10 + int(char)
            
            if char.isalpha():
                chars += char
            
            if char == "[":
                stack.append(chars)
                stack.append(nums)
                chars = ""
                nums = 0
            
            if char == "]":
                num = stack.pop()
                charStr = stack.pop()
                chars = charStr + (chars * num)
        return chars