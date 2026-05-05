class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str not in hashMap:
                hashMap[sorted_str] = [strs[i]]
            else:
                hashMap[sorted_str].append(strs[i])
        for values in hashMap.values():
            anagram = values
            output.append(values)
        return output