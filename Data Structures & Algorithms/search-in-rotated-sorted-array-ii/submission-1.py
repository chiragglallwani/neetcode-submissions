class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        # nums = list(set(nums))
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True

            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[m]: # left half is sorted, find in left half.
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return False