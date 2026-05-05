class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashTable = {}
        for char in s:
            hashTable[char] = hashTable.get(char, 0) + 1
        
        for char in t:
            if char in hashTable:
                char_count = hashTable.get(char)
                if char_count > 1:
                    hashTable[char] = char_count - 1
                else:
                    del hashTable[char]
        
        return True if len(hashTable) == 0 else False
