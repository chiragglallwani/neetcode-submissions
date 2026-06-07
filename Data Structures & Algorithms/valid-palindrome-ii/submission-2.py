class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Approach 1: use two pointers in opposite direction, if at any index,
        char is not same, then check for next index, if its then drop the element
        if this happen again and limit is used then return False
        """
        # limit = 1
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         if limit > 0:
        #             if s[left] == s[right - 1]:
        #                 right -= 1
        #             elif s[left + 1] == s[right]:
        #                 left += 1
        #             else:
        #                 return False
        #             limit -= 1
        #         else:
        #             return False
        #     left += 1
        #     right -= 1
        # return True
        """
        Approach 1 Failed, because unable to identify which element should be deleted, left or right?
        Approach 2: Since we don't know which one to delete hence we need to try both.
        """
        def is_validpalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (is_validpalindrome(left +1, right) or 
                is_validpalindrome(left, right - 1))
            left += 1
            right -= 1
        return True