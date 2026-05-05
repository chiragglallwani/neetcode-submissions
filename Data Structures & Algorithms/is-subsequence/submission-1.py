class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        tlen = len(t)
        slen = len(s)
        ptr1 = 0
        ptr2 = 0
        while ptr1 < tlen:
            if ptr2 == slen - 1:
                return True
            if t[ptr1] == s[ptr2]:
                ptr2 +=1
            ptr1 +=1
        return False