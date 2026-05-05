class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                total_product = math.prod(nums[i+1:])
                output.append(total_product)
            else:
                before_product = math.prod(nums[:i])
                after_product = math.prod(nums[i+1:])
                output.append(before_product * after_product)
        return output
        