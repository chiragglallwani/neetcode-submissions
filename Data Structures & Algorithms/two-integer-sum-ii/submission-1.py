class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        approch: We will be using two opposite pointer to solve this
        the array is sorted so doing the sum of left and right pointer
        compare that with target, if sum is less than target, then increase the left pointer
        else reduce the right pointer
        """
        left , right = 0, len(numbers) - 1
        while left < right:
            sumInteger = numbers[left] + numbers[right]
            if sumInteger == target:
                return [left + 1, right + 1]
            elif sumInteger < target:
                left +=1
            else:
                right -= 1
        return []