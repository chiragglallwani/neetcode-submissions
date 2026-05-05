class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = {}
        if len(s) != len(t):
            return False
        for char in s:
            hashTable[char] = hashTable.get(char, 0) + 1
        
        for char in t:
            if char in hashTable:
                 if hashTable.get(char) > 1:
                    hashTable[char] = hashTable.get(char) - 1
                 else:
                    del hashTable[char]
        return True if len(hashTable) == 0 else False