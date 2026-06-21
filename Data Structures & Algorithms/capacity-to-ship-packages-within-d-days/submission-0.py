class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Approach: First we need to find the start (lower bound) and end (higher bound) range to search for 
        exact least weight capacity.

        Start (Lower Bound) = max(weights) -> we can't break the package on ith day we need to transfer max weight into the shipWithinDays
        End (higher Bound) = sum(weights) we can transfer max sum of weights in 1 day.

        Implement Binary Search, get the mid (that is the expected max weight) -> iterate through weights, if on day ith sum of weights
        > mid, shift to next day. If total days is less than < D day then do mid + 1 to increase the load capacity else reduce the
        load capacity.
        """

        def isFeasible(weightList, capacity):
            day = 1
            currentLoad = 0
            for w in weightList:
                if currentLoad + w > capacity:
                    day += 1
                    currentLoad = w
                else:
                    currentLoad += w
            return day

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            needed = isFeasible(weights, mid)
            if needed > days:
                low = mid + 1
            else:
                high = mid # why not mid - 1 ?
        return low

