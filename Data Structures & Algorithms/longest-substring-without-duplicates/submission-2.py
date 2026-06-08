class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: variable sliding window problem, we use this approach because
        we will be using two pointers, right one to store in set, using left one
        to do ++ when right exist in the set and removed.
        longest_subStr is max of longest_subStr or right - left + 1
        """
        strSet = set()
        longest_subStr = 0
        left = 0
        for right in range( len(s)):
            while s[right] in strSet:
                strSet.remove(s[left])
                left += 1
            strSet.add(s[right])
            longest_subStr = max(longest_subStr, right - left + 1)
        return longest_subStr
        