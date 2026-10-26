class FreqStack:

    def __init__(self):
      self.stacks = {}
      self.count = {}
      self.maxCount = 0  

    def push(self, val: int) -> None:
        valueCount = 1 + self.count.get(val, 0)
        self.count[val] = valueCount

        if valueCount > self.maxCount:
            self.maxCount = valueCount
            self.stacks[valueCount] = []
        self.stacks[valueCount].append(val)

    def pop(self) -> int:
        result = self.stacks[self.maxCount].pop()
        self.count[result] -=1

        if not self.stacks[self.maxCount]:
            self.maxCount -= 1

        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()