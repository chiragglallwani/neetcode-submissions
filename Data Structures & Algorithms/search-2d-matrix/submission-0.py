class Solution:
    def binarySearch(self, nums: list[int], target:int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binarySearch(row, target)
        return False