class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_arr = set()
        for i in range(len(nums)):
            if (nums[i] in unique_arr):
                return True
            else:
                unique_arr.add(nums[i])

        return False