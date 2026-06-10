class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: variable sliding window problem, we use this approach because
        we will be using two pointers, right one to store in set, using left one
        to do ++ when right exist in the set and removed.
        longest_subStr is max of longest_subStr or right - left + 1
        """
        strSet = set()
        left = 0
        right = 0
        maxLen = 0
        while right < len(s):
            while s[right] in strSet:
                strSet.remove(s[left])
                left += 1
            strSet.add(s[right])
            right += 1
            maxLen = max(maxLen, right - left)

        return maxLen
        