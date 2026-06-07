class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        Approach: use two pointer in opposite direction and swap the elements
        """
        if len(s) == 1:
            return
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -= 1
        