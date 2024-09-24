# T: O(1)
# S: O(n) - maxes
class MaxStack:
    def __init__(self):
        self.values = []
        self.maxes = []

    def push(self, el):
        self.values = self.values + [el]
        if not self.maxes or el > self.maxes[-1]:
            self.maxes.append(el)
        else:
            self.maxes.append(self.maxes[-1])

    def pop(self):
        last_el = self.values[-1]
        self.values = self.values[:-1]
        self.maxes = self.maxes[:-1]
        return last_el

    def max(self):
        return self.maxes[-1]


stack = MaxStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)
print(stack.max())

print(stack.pop())
print(stack.pop())
print(stack.max())

stack.push(5)
stack.push(2)
print(stack.max())
