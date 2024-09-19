class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# T: O(n) - max len l1 or l2
# S: O(n) - 1 list
class Solution:
    def _add_two_numbers_helper(self, l1, l2):
        l1_current = l1
        l2_current = l2
        carryover = 0
        l3_result = l3_current_node = None

        while l1_current or l2_current:
            val1 = l1_current.val if l1_current else 0
            val2 = l2_current.val if l2_current else 0
            sum_val = val1 + val2 + carryover
            carryover = sum_val // 10
            sum_remainder = sum_val % 10
            if not l3_result:
                l3_result = l3_current_node = LinkedListNode(sum_remainder)
            else:
                l3_current_node.next = LinkedListNode(sum_remainder)
                l3_current_node = l3_current_node.next
            l1_current = l1_current.next if l1_current and l1_current.next else None
            l2_current = l2_current.next if l2_current and l2_current.next else None
        if carryover > 0:
            l3_current_node.next = LinkedListNode(carryover)
        return l3_result

    def add_numbers(self, l1, l2):
        return self._add_two_numbers_helper(l1, l2)

l1 = LinkedListNode(2)
l1.next = LinkedListNode(4)
l1.next.next = LinkedListNode(3)

l2 = LinkedListNode(5)
l2.next = LinkedListNode(6)
l2.next.next = LinkedListNode(4)

l3 = Solution().add_numbers(l1, l2)

while l3:
    print(l3.val)
    l3 = l3.next
