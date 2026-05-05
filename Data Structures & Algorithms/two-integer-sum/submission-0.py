class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            second_sum = target - nums[i]
            if second_sum in hashMap:
                return [hashMap[second_sum], i]
            else:
                hashMap[nums[i]] = i
        return [0,0]