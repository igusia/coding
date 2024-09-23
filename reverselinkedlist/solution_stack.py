class Node:
    def __init__(self, val, next_pointer=None):
        self.val = val
        self.next_pointer = next_pointer


# T: O(n)
# S: O(n)
class Solution:
    def reverse(self, li):
        stack = []
        while li:
            stack.append(li.val)
            li = li.next_pointer
        res = Node(stack.pop())
        curr_pointer = res
        while stack:
            curr_pointer.next_pointer = Node(stack.pop())
            curr_pointer = curr_pointer.next_pointer
        return res


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
result = Solution().reverse(node)
while result:
    print(result.val)
    result = result.next_pointer
