class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # maxArea = 0
        # stack = []
        # for i in range(n + 1):
        #     while stack and (i == n or heights[stack[-1]] >= heights[i]): 
        #         # current index is last index or last stored height in stack >= current height
        #         height = heights[stack.pop()]
        #         width = i if not stack else i - stack[-1] - 1
        #         maxArea = max(maxArea, height * width)
        #     stack.append(i)
        # return maxArea
        
        """
        Approach: iterate through heights & insert into the stack the height (which is continued)
        and index as pair. Untill heights[i] < stack[-1] height then we need to calculate the 
        maxArea rectangle.

        At end, we will still be having the stack content left so we need to calculate
        the rectangle area for that as well & compare to maxArea
        """
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # stack last element height is greater than current height, hence max rectangle area formed for past elements.
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


