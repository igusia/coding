class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n)
# S: O(n)
class Solution:
    def _is_valid_bst_helper(self, n, low, high):
        if not n:
            return True
        val = n.val
        return (low < val < high and
                self._is_valid_bst_helper(n.left, low, val) and
                self._is_valid_bst_helper(n.right, val, high))

    def is_valid_bst(self, n):
        return self._is_valid_bst_helper(n, float('-inf'), float('inf'))


#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)

print(Solution().is_valid_bst(node))
