class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        output = [[1], [1,1]]

        for row in range(2, numRows):
            current_row = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    current_row.append(1)
                else:
                    current_row.append(output[row-1][col-1] + output[row-1][col])
            output.append(current_row)
        return output
