class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """
        Approach: Think of it as two sorted array merged together, first half ascending order and
        second half is descending order.
        Step 1: Find the peak of the mountain.
        Step 2: Find the target in ascending array, if not found return -1
        Step 3: Find the target in descending array, if not found return -1
        """

        def findAscenArr(ascleft, ascright) -> int:
            found_index_asc = -1 
            while ascleft <= ascright:
                m = (ascleft + ascright) // 2
                if target <= mountainArr.get(m):
                    found_index_asc = m
                    ascright = m - 1
                else:
                    ascleft = m + 1
            if found_index_asc != -1 and mountainArr.get(found_index_asc) == target:
                return found_index_asc
            return -1
        
        def findDescendArr(descleft, descright) -> int:
            found_index_desc = -1
            while descleft <= descright:
                m = (descleft + descright) // 2
                if target >= mountainArr.get(m):
                    found_index_desc = m
                    descright = m - 1
                else:
                    descleft = m + 1
            if found_index_desc != -1 and mountainArr.get(found_index_desc) == target:
                return found_index_desc
            return -1


        # Step 1: Find the peak of the array mountainArr.get(m) <= mountainArr.get(mid + 1) -> left += 1 else right -= 1
        start, end = 0,  mountainArr.length() - 1
        l,r = start, end
        peak_index = -1
        while l <= r:
            m = (l + r) // 2
            if m < r and mountainArr.get(m) > mountainArr.get(m + 1):
                peak_index = m
                r = m - 1
            else:
                l = m + 1
        
        # Step 2: Find the target element now in first half, if found return the index else -1
        result = findAscenArr(start,peak_index)
        if result == -1:
            result = findDescendArr(peak_index + 1, end)

        return result