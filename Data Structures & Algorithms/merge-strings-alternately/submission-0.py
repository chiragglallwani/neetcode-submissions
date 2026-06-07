class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Approach 1: Take the longest substring, iterate through for loop, 
        check if the ith index is less than the other string index, then insert else skipp that
        """

        n = max(len(word1), len(word2))
        stringList = []
        for i in range(n):
            if i < len(word1):
                stringList.append(word1[i])
            if i < len(word2):
                stringList.append(word2[i])
        return "".join(stringList)
