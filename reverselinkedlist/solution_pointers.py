class Node:
    def __init__(self, val, next_pointer=None):
        self.val = val
        self.next_pointer = next_pointer


# T: O(n)
# S: O(1)
class Solution:
    def reverse(self, li):
        if not li:
            return li
        curr = li
        prev = None
        while curr:
            tmp = curr.next_pointer
            curr.next_pointer = prev
            prev = curr
            curr = tmp
        return prev


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
result = Solution().reverse(node)
while result:
    print(result.val)
    result = result.next_pointer
