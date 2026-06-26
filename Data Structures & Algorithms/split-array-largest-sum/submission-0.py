class Solution:
    def isFeasible(self, nums:List[int], k:int, midSum:int) -> bool:
        segment = 1
        currSum = 0
        for num in nums:
            if currSum + num > midSum:
                segment += 1
                currSum = num
            else:
                currSum += num
        print(segment)
        return segment <= k
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if self.isFeasible(nums, k, m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res