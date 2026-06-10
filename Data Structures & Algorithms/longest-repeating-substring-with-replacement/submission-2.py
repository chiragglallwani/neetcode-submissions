class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Approach: keep adding/updating the frequency of character in countMap
        check if the window size - maxFrequency (max of the most repeated chars in map) > k
        then that means, in the given windowSize (l - r + 1) there is more chars then
        we can replace hence reduce the windowsize by moving l++ & repeat the process.
        Summary: increase the window size untill in the given window, 
        length of window - maxrepetition of char in that window < k
        if this breaks, reduce the size of window and do again 
        """
        
        # countMap ={}
        # left = 0
        # maxCharF = 0
        # result = 0
        # for right in range(len(s)):
        #     countMap[s[right]] = 1 + countMap.get(s[right], 0)
        #     maxCharF = max(maxCharF, countMap[s[right]])
            
        #     while (right - left + 1) - maxCharF > k:
        #         countMap[s[left]] -= 1
        #         left += 1
        #     result = max(result, right - left + 1)
        # return result
        charCountMap = {}
        l = 0
        maxLen = 0
        max_char_count_in_window = 0
        for r in range(len(s)):
            charCountMap[s[r]] = 1 + charCountMap.get(s[r], 0)
            max_char_count_in_window = max(max_char_count_in_window,  charCountMap[s[r]])
            while r - l + 1 - max_char_count_in_window > k:
                charCountMap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            