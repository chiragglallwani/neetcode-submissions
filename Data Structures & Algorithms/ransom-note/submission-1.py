class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in magazine:
            if len(ransomNote) == 0:
                return True
            if char in ransomNote:
                ransomNote = ransomNote.replace(char, "", 1)
        return True if len(ransomNote) == 0 else False