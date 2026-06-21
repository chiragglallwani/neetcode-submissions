class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left +=1
        #     else:
        #         right -=1
        # return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1