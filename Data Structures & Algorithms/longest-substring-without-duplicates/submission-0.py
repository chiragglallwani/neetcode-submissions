class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left +=1
            charSet.add(s[right])
            sub_str = max(sub_str, right - left + 1)
        return sub_str