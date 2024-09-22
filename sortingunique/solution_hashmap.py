unique_nums = [1, 2, 3]


# T: O(n)
# S: O(size of returned array) + O(size of unique numbers) = O(n)
class Solution:
    def _build_sorted_helper(self, counts, i):
        return [unique_nums[i]] * counts.get(unique_nums[i], 0)

    def sort(self, arr):
        if not arr:
            return arr
        counts = {}
        for element in arr:
            if element in counts.keys():
                counts[element] += 1
            else:
                counts[element] = 1
        return [item for i in range(len(unique_nums)) for item in self._build_sorted_helper(counts, i)]


arr = [3, 3, 2, 1, 3, 2, 1]
print(Solution().sort(arr))
