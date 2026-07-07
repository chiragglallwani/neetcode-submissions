class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if len(nums) == 0:
        #     return 0
        # count = 0
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[left] == val: # if we get val in start ith of the array we will put them at last
        #         while nums[right] == val and right > left: #but we will check if the last element is not equals to val
        #             right -=1 # if it is, then find the element not equal to val by moving the pointer to the right.
        #         nums[left], nums[right] = nums[right], nums[left] # once we find element from right not equal to Val, swap it
        #         count +=1 # increase the count by 1 because we have now found one more element from left which is not equal to val.
        #     else:
        #         count +=1 # increase the count by 1 as we the element at left pointer is not equal to val.
        #     left +=1
        # if nums[right] != val: # At last but not least, when left pointer is just before the right pointer, 
        #                     # we need to check if the element at right pointer is not equal to val, if not then count + 1
        #     count +=1
        # return count

        if len(nums) == 0:
            return 0
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == val:
                while left < right and nums[right] == val:
                    right -= 1
                if nums[right] != val:
                    nums[left], nums[right] = nums[right], nums[left]
                    count += 1
                    left += 1
                print(left)
                print(count)
            else:
                count += 1
                left += 1
        
        if nums[right] != val:
            count += 1
        
        return count
                