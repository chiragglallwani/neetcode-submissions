class Solution:
    def isOpposite(self, as1:int, as2:int) -> bool:
        return True if (as2 < 0 and as1 > 0) else False
                        
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and self.isOpposite(stack[-1], asteroid):
                diff = asteroid + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    stack.pop()
            if asteroid:
                stack.append(asteroid)

        return stack