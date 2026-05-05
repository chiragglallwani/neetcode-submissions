class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_text = "".join(char for char in s if char.isalnum())
        left, right = 0, len(filter_text) - 1
        while left < right:
            if filter_text[left].lower() == filter_text[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True
        