class Solution:
    def validWindow(self, subStr: str, hashMap: dict[str, int], n: int) -> bool:
        count = 0
        copyHashMap = dict(hashMap)
        if len(subStr) < n:
            return False
        for i in range(len(subStr)):
            if subStr[i] in copyHashMap:
                copyHashMap[subStr[i]] -= 1
                if copyHashMap[subStr[i]] <= 0:
                    del copyHashMap[subStr[i]]
                count += 1
            
        return count == n
    def minWindow(self, s: str, t: str) -> str:
        # if t == "":
        #     return ""

        # countT, window = {}, {}
        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)

        # have, need = 0, len(countT)
        # res, resLen = [-1, -1], float("infinity")
        # l = 0
        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         if (r - l + 1) < resLen:
        #             res = [l, r]
        #             resLen = r - l + 1

        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1
        # l, r = res
        # return s[l : r + 1] if resLen != float("infinity") else ""
        if len(t) > len(s):
            return ""
        hashMap = {}
        minStrLength = float("inf")
        l = 0
        finalResult = ""
        for i in range(len(t)):
            hashMap[t[i]] = 1 + hashMap.get(t[i], 0)
        for r in range(len(s)):
            while self.validWindow(s[l:r+1], hashMap, len(t)):
                # print("I am a valid window", s[l:r+1])
                if r - l + 1 < minStrLength:
                    # print("I am a min String", s[l:r + 1])
                    finalResult = s[l:r + 1]
                    minStrLength = r - l + 1
                l += 1
        return finalResult
