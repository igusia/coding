# T: O(n)
# S: O(1)
class Solution:
    def determine_non_decreasing(self, nums):
        if not nums or len(nums) < 3:
            return True

        counter_modifications_needed = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                counter_modifications_needed += 1

                if counter_modifications_needed > 1:
                    return False

                if i > 1 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]

        return True


arr_1 = [3, 2, 4, 1]
arr_2 = [-1, 4, 2, 3]
print(Solution().determine_non_decreasing(arr_1))
print(Solution().determine_non_decreasing(arr_2))
