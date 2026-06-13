class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maxList = [max(nums[0:k])]
        # for right in range(k, len(nums)):
        #     left = right - k
        #     maxNum = max(nums[left+1:right+1])
        #     maxList.append(maxNum)
        # return maxList
        result = [max(nums[:k])]
        for r in range(k, len(nums)):
            l = r - k
            result.append(max(nums[l+1:r+1]))
        return result
        