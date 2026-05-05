class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        output = []
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        sortedList = dict(sorted(hashMap.items(), key=lambda item: item[1]))
        return list(sortedList.keys())[-k:]
