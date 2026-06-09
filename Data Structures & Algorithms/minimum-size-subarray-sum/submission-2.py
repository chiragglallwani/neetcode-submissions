class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Approach: Failed approach because it unable to return only 1 as 
        length
        """
        # left = 0
        # arrSum = nums[left]
        # minLength = float('inf')
        # for right in range(len(nums)):
        #     arrSum += nums[right]
        #     while arrSum > target and left < right:
        #         arrSum -= nums[left]
        #         if arrSum < target:
        #             minLength = min(minLength, right - left + 1)
        #         left += 1
        #     if arrSum == target:
        #         minLength = min(minLength, right - left + 1)
        # return 0 if minLength == float("inf") else int(minLength)

        """
        Approach: same as above just with minor tweaks
        """
        left = 0
        arrSum = 0 # initial Sum should be zero
        minLength = float('inf')
        for right in range(len(nums)):
            arrSum += nums[right]
            while arrSum >= target:
                minLength = min(minLength, right - left + 1)
                arrSum -= nums[left]     
                left += 1
        return 0 if minLength == float("inf") else int(minLength)

