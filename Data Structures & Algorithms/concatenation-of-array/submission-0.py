class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_len = len(nums) * 2
        ans = [0] * ans_len
        n = len(nums)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans