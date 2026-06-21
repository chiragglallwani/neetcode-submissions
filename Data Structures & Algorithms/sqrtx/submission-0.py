class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        min_sqrt = float("inf")
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            squareof_mid = mid * mid
            print(squareof_mid)
            if squareof_mid == x:
                return mid
            elif squareof_mid < x:
                l = mid + 1
                min_sqrt = max(min_sqrt, mid)
            else:
                r = mid - 1
            min_sqrt = min(min_sqrt, mid)
           
        return int(min_sqrt)