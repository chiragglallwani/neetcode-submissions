class Solution:
    def findMaxNum(self, arr: List[int]) -> int:
        return sorted(arr)[-1]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = [self.findMaxNum(nums[0: k])]
        for right in range(k, len(nums)):
            left = right - k
            maxNum = self.findMaxNum(nums[left+1:right+1])
            maxList.append(maxNum)
        return maxList
        