class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        if len(s) != len(t):
            return False
        hashTable = {}
        output = ""

        for i in range(len(s)):
            if s[i] not in hashTable:
                if not self.check_if_map_value_exist(t[i], hashTable):
                    hashTable[s[i]] = t[i]
                else:
                    hashTable[s[i]] = " "
        
        for value in s:
            output += hashTable.get(value)

        return output == t
    
    def check_if_map_value_exist(self, char: str, hashTable: dict) -> bool:
        for value in hashTable.values():
            if char == value:
                return True
        return False
        

        