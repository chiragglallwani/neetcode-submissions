class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Approach: Two pointer in opposite direction. Calculate its volumne, compare that with max volume. 
        if the left container height is smaller, do left +=1 else right -=1
        """
        maxVolume = 0
        left, right = 0, len(heights) - 1
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            maxVolume = max(volume, maxVolume)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return maxVolume