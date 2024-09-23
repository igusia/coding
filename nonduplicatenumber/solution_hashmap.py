# T: O(n) - 2 iterations
# S: O(n)
class Solution:
    def find_non_duplicate(self, nums):
        num_counts = {}
        for num in nums:
            if num in num_counts.keys():
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        for k, v in num_counts.items():
            if v == 1:
                return k
        return None


arr = [4, 3, 2, 4, 1, 3, 2]
print(Solution().find_non_duplicate(arr))
