class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashMap= {}
        output = []
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word not in hashMap:
                hashMap[sorted_word] = [strs[i]]
            else:
                hashMap[sorted_word].append(strs[i])
        for value in hashMap.values():
            output.append(value)

        return output