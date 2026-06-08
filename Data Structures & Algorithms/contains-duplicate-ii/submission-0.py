class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Approach: Hashmap to store the elements in map, see in when element is in map and its
        calc = (i - j) <= k
        """
        hMap = {}
        for i in range(len(nums)):
            if nums[i] in hMap and i - hMap[nums[i]] <= k:
                return True
            hMap[nums[i]] = i
        return False