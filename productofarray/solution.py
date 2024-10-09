# T: O(n)
# S: O(n)
class Solution:
    def solve_product_except_self(self, nums):
        results = [1] * len(nums)
        left_total_product = 1
        right_total_product = 1
        for i in range(len(nums)):
            results[i] = left_total_product
            left_total_product = left_total_product * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            results[i] = results[i] * right_total_product
            right_total_product = right_total_product * nums[i]
        return results


arr = [1, 2, 3, 4]
print(Solution().solve_product_except_self(arr))
