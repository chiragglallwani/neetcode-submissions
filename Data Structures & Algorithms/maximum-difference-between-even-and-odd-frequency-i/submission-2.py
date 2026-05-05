class Solution:
    def maxDifference(self, s: str) -> int:
        hashTable = {}
        max_diff = 0

        for char in s:
            hashTable[char] = hashTable.get(char, 0) + 1
        
        freq_sorted = sorted(hashTable.values())
        min_even = min_odd = float("inf")
        max_even = max_odd = float("-inf")
        
        for num in freq_sorted:
            if num % 2 == 0:
                min_even = min(min_even, num)
                max_even = max(max_even, num)
            else:
                min_odd = min(min_odd, num)
                max_odd = max(max_odd, num)
        # Check the two possible extreme differences
        diff1 = min_odd - min_even
        diff2 = max_odd - min_even
        
        return max(diff1, diff2)