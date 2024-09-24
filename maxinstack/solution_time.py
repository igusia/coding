# T: O(n) - 1 iteration to find max
# S: O(1) - no new structure when finding max
class MaxStack:
    def __init__(self):
        self.values = []

    def push(self, el):
        self.values = self.values.append(el)

    def pop(self):
        if not self.values:
            return None
        last_el = self.values[-1]
        self.values = self.values[:-1]
        return last_el

    def max(self):
        max_el = None
        for el in self.values:
            if not max_el or el > max_el:
                max_el = el
        return max_el


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
