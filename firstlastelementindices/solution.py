# T: O(log(n)) - 2 binary searches
# S: O(1)
class Solution:
    def _binary_search_helper(self, numbers, target, first):
        low = 0
        high = len(numbers) - 1
        while True:
            if high < low:
                return -1
            mid = (low + high) // 2
            if first:
                if numbers[mid] == target and (mid == 0 or target > numbers[mid - 1]):
                    return mid
                elif target > numbers[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if numbers[mid] == target and (mid == (len(numbers) - 1) or numbers[mid + 1] > target):
                    return mid
                elif target < numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

    def _binary_search_first(self, numbers, target):
        return self._binary_search_helper(numbers, target, True)

    def _binary_search_last(self, numbers, target):
        return self._binary_search_helper(numbers, target, False)

    def find_indices(self, numbers, target):
        first = self._binary_search_first(numbers, target)
        last = self._binary_search_last(numbers, target)
        return [first, last]


numbers = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
print(Solution().find_indices(numbers, target))
