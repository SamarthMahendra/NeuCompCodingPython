import math
class MinStack:

    def __init__(self):
        self.minimum = []
        self.m = math.inf
        self.stack = []

    def push(self, val: int) -> None:
        self.m = min(val, self.m)
        self.minimum.append(self.m)
        self.stack.append(val)

    def pop(self) -> None:
        self.minimum.pop()
        if self.minimum == []:
            self.m = math.inf
        else:
            self.m = self.minimum[-1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m


# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print(obj.top())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
obj.push(2147483647)
print(obj.top())
print(obj.getMin())
obj.push(-2147483648)
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())

