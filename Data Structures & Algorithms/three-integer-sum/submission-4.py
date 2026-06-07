class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach1: Use three for loops of i,j,k and check if sum = 0 then store
        into the triplet array. Time Complexity: O(N^3)
        Approach2: Here, sorting is "Important". Use one for loop to iterate over all the elements in the array
        and use two pointers in oppposite direction to iterate and check sum.
        """
        target = 0
        tripletArr = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == target:
                    sumList = [nums[i], nums[left], nums[right]]
                    if sumList not in tripletArr:
                        tripletArr.append(sumList)
                    left += 1
                    right -= 1
                elif threeSum > target:
                    right -= 1
                else:
                    left += 1
        return tripletArr
                

