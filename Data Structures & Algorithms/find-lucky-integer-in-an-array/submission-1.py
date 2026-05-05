class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashMap = {}
        maxNum = -1
        for num in arr:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for key, value in hashMap.items():
            if key == value and key > maxNum:
                maxNum = key

        return maxNum