unique_nums = [1, 2, 3]


# T: O(n)
# S: O(1)
class Solution:
    def _swap_elements(self, arr, index_min, index_max):
        arr[index_min], arr[index_max] = arr[index_max], arr[index_min]

    def sort(self, arr):
        pointer_min = 0
        pointer_max = len(arr) - 1
        min_el = min(arr)
        max_el = max(arr)
        index = 0
        while index <= pointer_max:
            if arr[index] == min_el:
                self._swap_elements(arr, index, pointer_min)
                pointer_min += 1
                index += 1
            elif arr[index] == max_el:
                self._swap_elements(arr, index, pointer_max)
                pointer_max -= 1
            else:
                index += 1
        return arr


arr = [3, 3, 2, 1, 3, 2, 1]
print(Solution().sort(arr))
