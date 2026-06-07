class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Approach: Use two pointer at index 1 (i, j), we will now check if a[j] != a[i-1] => Not a duplicated
        then place a[i] = a[j], i++
        return i at the end 
        """
        if len(nums) == 1:
            return 1
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i +=1
        return i