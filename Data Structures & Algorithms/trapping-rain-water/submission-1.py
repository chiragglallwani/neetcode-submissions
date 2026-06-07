class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: View this tutorial: https://www.youtube.com/watch?v=ZI2z5pq0TqA
        On high level, we need to use two pointer approach in opposite direction, 
        we will store maxL = max(maxL, height[left]) & maxR = max(maxR, height[right])
        whichever of maxL or maxR is smaller that pointer will be moved. 
        We will do the calculation like storage = maxL - height[left] and add to total_storage
        likewise for the right one as well, untill left pointer cross the right part or vice versa
        """
        if not height:
            return 0
        left_ptr, right_ptr = 0, len(height) - 1
        maxL, maxR = height[left_ptr], height[right_ptr]
        total_water = 0
        while left_ptr < right_ptr:
            if maxL < maxR:
                left_ptr +=1
                maxL = max(maxL, height[left_ptr])
                total_water += maxL - height[left_ptr]
            else:
                right_ptr -= 1
                maxR = max(maxR, height[right_ptr])
                total_water += maxR - height[right_ptr]
        return total_water
