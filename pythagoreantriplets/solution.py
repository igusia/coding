import math


# T: O(n^2)
# S: O(n)
class Solution:
    def create_squares(self, nums):
        return set([num * num for num in nums])

    def find_triplets(self, nums):
        ret = set()
        if not nums or len(nums) < 3:
            return ret
        nums_squared = self.create_squares(nums)
        for num_i in nums:
            for num_j in nums:
                result = num_i * num_i + num_j * num_j
                if num_i < num_j and result in nums_squared:
                    ret.add(tuple([num_i, num_j, math.floor(math.sqrt(result))]))
        return ret


arr = [3, 5, 12, 5, 13]
print(Solution().find_triplets(arr))
