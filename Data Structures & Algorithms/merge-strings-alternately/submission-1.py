class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Approach 1: Take the longest substring, iterate through for loop, 
        check if the ith index is less than the other string index, then insert else skipp that
        """

        # n = max(len(word1), len(word2))
        # stringList = []
        # for i in range(n):
        #     if i < len(word1):
        #         stringList.append(word1[i])
        #     if i < len(word2):
        #         stringList.append(word2[i])
        # return "".join(stringList)

        """
        Approach 2: use two pointer w1 and w2, iterate w1 from word1 and w2 from word2
        if it ends then iterate through rest of the words
        """
        w1, w2 = 0,0
        result = ""
        while w1 < len(word1) and w2 < len(word2):
            result += word1[w1]
            result += word2[w2]
            w1 +=1
            w2 +=1
        result += word1[w1:]
        result += word2[w2:]
        return result

