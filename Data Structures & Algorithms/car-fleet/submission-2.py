class Solution:
    def getTime(self, target: int, start: int, speed:int) -> float:
        distance = target - start
        return distance / speed
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(p, s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)
        # stack = []
        # for p, s in pair:  # Reverse Sorted Order
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)
        hashMap = {}
        for index in range(len(position)):
            time = self.getTime(target, position[index], speed[index])
            hashMap[position[index]] = time
        hashMap = dict(sorted(hashMap.items(), reverse=True))
        stack = []
        for v in hashMap.values():
            if not stack:
                stack.append(v)
            if stack and stack[-1] < v:
                stack.append(v)
        return len(stack)
    
