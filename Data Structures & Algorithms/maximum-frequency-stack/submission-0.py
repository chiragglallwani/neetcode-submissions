from collections import Counter, defaultdict
class FreqStack:

    def __init__(self):
        self.frequency_map = Counter()
        self.group_num_by_frequency = defaultdict(list) #creates empty list for key automatically.
        self.max_frequency = 0
    def push(self, val: int) -> None:
       val_frequency = self.frequency_map[val] + 1

       self.frequency_map[val] = val_frequency # set the frequency of value in map

       if val_frequency > self.max_frequency:
            self.max_frequency = val_frequency
       
       # we will add the val to list based on the max_frequency
       self.group_num_by_frequency[val_frequency].append(val) 


    def pop(self) -> int:
        #pop the last item from list of max_frequency key in group_num_by_frequency
        val = self.group_num_by_frequency[self.max_frequency].pop()


        self.frequency_map[val] -= 1

        if not self.group_num_by_frequency[self.max_frequency]:
            self.max_frequency -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()