class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         Set the search range:
# left = 1 (minimum possible speed)
# right = max(piles) (maximum needed speed)
# While left <= right:
# Let mid be the current speed to test.
# Compute the total hours needed using this speed.
# If the total hours is within the allowed time h:
# This speed works, so record it.
# Try to find a smaller working speed by searching the left half.
# Otherwise:
# Speed is too slow, so search in the right half.
# After the search ends, return the smallest valid speed found.

        # l, r = 1, max(piles)
        # res = 0
        # while l <= r:
        #     k = (l + r) // 2
        #     totalTime = 0
        #     for p in piles:
        #         totalTime += math.ceil(float(p) / k)
        #     if totalTime <= h:
        #         res = k
        #         r = k - 1
        #     else:
        #         l = k + 1
        # return res

        def isFeasible(mid):
            hours = 0
            for banana in piles:
                hours += math.ceil(float(banana)/mid)
            return hours <= h

        l, r = 1, max(piles)
        hrs_rate = 0
        while l <= r:
            mid = l + (r - l) // 2
            if isFeasible(mid):
                hrs_rate = mid
                r = mid - 1
            else:
                l = mid + 1
        return hrs_rate



