# T: O(n) - 1 iteration
# S: O(1)
class Solution:
    def xor_nums(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique


arr = [4, 3, 2, 4, 1, 3, 2]
print(Solution().xor_nums(arr))
