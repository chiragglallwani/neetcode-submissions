class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = [max(nums[0:k])]
        for right in range(k, len(nums)):
            left = right - k
            maxNum = max(nums[left+1:right+1])
            maxList.append(maxNum)
        return maxList
        