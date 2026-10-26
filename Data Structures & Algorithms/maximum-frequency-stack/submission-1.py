#Frequency Array

class FreqStack:

    def __init__(self):
        self.stacks = [[]]
        self.count = {}        

    def push(self, val: int) -> None:
        valueCount = 1 + self.count.get(val, 0)
        self.count[val] = valueCount
        if valueCount == len(self.stacks):
            self.stacks.append([])
        self.stacks[valueCount].append(val)

    def pop(self) -> int:
        result = self.stacks[-1].pop()
        self.count[result] -= 1

        if not self.stacks[-1]:
            self.stacks.pop()

        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()