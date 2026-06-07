class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: use 2 loops and 2 pointers, keep in mind that we don't want to add duplicate arrays
        therefore check if i , j are greater than 0 and i + 1, l < r then check if a[l] == a[l-1] or if a[l] == a[r + 1] then l += 1 and r -= 1
        """
        fourSumArr = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l , r = j + 1, len(nums) - 1
                while l < r:
                    fpointerSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fpointerSum == target:
                        fourSumArr.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif fpointerSum < target:
                        l += 1
                    else:
                        r -= 1
        return fourSumArr