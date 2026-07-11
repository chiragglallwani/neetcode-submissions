# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        for i in range(len(pairs)):
            temp = pairs[i]
            tempKey = temp.key
            previous = i - 1
            while previous >= 0 and pairs[previous].key > tempKey:
                pairs[previous + 1] = pairs[previous]
                previous -= 1
            pairs[previous + 1] = temp
            output.append(pairs[:]) # snapshot copy
        return output