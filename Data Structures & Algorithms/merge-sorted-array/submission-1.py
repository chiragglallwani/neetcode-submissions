class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Approach: Using 3 pointer approach ptr1 should be m -1, ptr2 should be len(nums1) - 1 and ptr3 should be n -1
        We need to check if ptr1 and ptr3 are greater than zero, then compare which of the element on that pointer is greater fill that from end.
        reduce that pointer and ptr2. If any of them becomes negative, skip that pointer & fill rest of the loop with other pointer.
        """
        ptr1, ptr2, ptr3 = m - 1, len(nums1) - 1, n -1
        while ptr2 >= 0:
            if ptr1 >= 0 and ptr3 >= 0:
                if nums1[ptr1] >= nums2[ptr3]:
                    nums1[ptr2] = nums1[ptr1]
                    ptr1 -= 1
                else:
                    nums1[ptr2] = nums2[ptr3]
                    ptr3 -= 1
            elif ptr1 >= 0 and ptr3 < 0:
                nums1[ptr2] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr2] = nums2[ptr3]
                ptr3 -= 1
            ptr2 -= 1
        
        