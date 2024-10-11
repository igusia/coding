class Solution:
    def determine_non_decreasing(self, nums):
        if not nums or len(nums) < 3:
            return True
        err = False
        for i in range(1, len(nums) - 2):
            if (nums[i - 1] < nums[i]) and (nums[i] > nums[i + 1]) and (nums[i + 1] < nums[i + 2]) and (nums[i - 1] > nums[i + 1]):
                err = True
            elif nums[i - 1] > nums[i] > nums[i + 1]:
                err = True
        i = len(nums) - 2
        err = err or nums[i - 1] > nums[i] > nums[i + 1]
        return not err


arr_1 = [1, 3, 2]
arr_2 = [-1, 4, 2, 3]
print(Solution().determine_non_decreasing(arr_1))
print(Solution().determine_non_decreasing(arr_2))
