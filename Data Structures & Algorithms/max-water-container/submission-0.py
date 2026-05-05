class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterVolume = 0
        left_ptr, right_ptr = 0, len(heights) - 1
        while left_ptr < right_ptr:
            maxVolume = (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr])
            maxWaterVolume = max(maxWaterVolume, maxVolume)
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return maxWaterVolume