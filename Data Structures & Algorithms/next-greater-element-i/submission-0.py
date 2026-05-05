class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        output = []
        for i in range(len(nums2)):
            max_num = nums2[i]
            for j in range (i+1, len(nums2)):
                if nums2[j] > max_num:
                    max_num = nums2[j]
                    break
            if max_num != nums2[i]:
                hashMap[nums2[i]] = max_num
            else:
                hashMap[nums2[i]] = -1
        
        for num in nums1:
            output.append(hashMap.get(num))
        return output