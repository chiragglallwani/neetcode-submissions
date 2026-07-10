class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Descision Tree making Approach
        """
        hashMap = {}
        def solve(num: int) -> int:
            if num == 0:
                return 1
            if num < 0:
                return 0
            if num in hashMap:
                return hashMap[num]
            hashMap[num] = solve(num-1) +  solve(num-2)
            return hashMap[num]
        return solve(n)

