class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = sorted(nums)
        tripletList = []
        for first_ptr in range(len(sortedList)):
            left, right = first_ptr + 1, len(sortedList) - 1
            while left < right:
                threeSum = sortedList[first_ptr] + sortedList[left] + sortedList[right]
                if threeSum == 0:
                    sumList = [sortedList[first_ptr], sortedList[left], sortedList[right]]
                    if sumList not in tripletList:
                        tripletList.append(sumList)
                    left +=1
                    right-=1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
        return tripletList
