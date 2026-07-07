class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # max_right = -1
        # for i in range (n - 1, -1, -1):
        #     new_val = max_right
        #     max_right = max(max_right, arr[i])
        #     arr[i] = new_val
        # return arr
        """
        Approach: Iterate from end of array, get the value at index i from end
        compare it with max value, which will be your next_max value.
        Set that max_value when iterating backwards
        """

        end = len(arr) - 1
        maxValue = -1
        while end >= 0:
            curr_value = arr[end]
            new_max_value = max(curr_value, maxValue)
            arr[end] = maxValue
            maxValue = new_max_value
            end -= 1
        return arr