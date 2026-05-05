class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and nums[0] == nums[1]:
            return [0,1]
        
        hashTable = {}
        for i in range(len(nums)):
            rest_value = target - nums[i];
            if rest_value in hashTable:
                return [hashTable.get(rest_value), i]
            else:
                hashTable[nums[i]] = i
        return []


