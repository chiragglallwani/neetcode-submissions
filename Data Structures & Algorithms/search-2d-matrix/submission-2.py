class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ROWS, COLS = len(matrix), len(matrix[0])

        # l, r = 0, ROWS * COLS - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     row, col = m // COLS, m % COLS
        #     if target > matrix[row][col]:
        #         l = m + 1
        #     elif target < matrix[row][col]:
        #         r = m - 1
        #     else:
        #         return True
        # return False
        """
        Approach: Imagine this 2D array has flat Array, then calculate the mid
        point. Then we need to find row and col of that mid index.
        This can be found with row = m // COLS, col = m % COLS.
        why m // COLS ? -> this reutrns the floor divisible value stating the
        row. m % COLS returns the remaninder in that row.
        """

        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // len(matrix[0]), m % len(matrix[0])
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        return False