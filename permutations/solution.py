# T: O(n!)
# S: O(n!)
class Solution:
    def _swap_elements(self, numbers, start_index, index):
        numbers[index], numbers[start_index] = numbers[start_index], numbers[index]

    def _find_permutations_helper(self, numbers, start_index=0):
        if start_index == len(numbers):
            return [numbers[:]]
        permutations = []
        used = []
        for i in range(start_index, len(numbers)):
            if numbers[i] not in used:
                self._swap_elements(numbers, start_index, i)
                permutations.extend(self._find_permutations_helper(numbers, start_index + 1))
                self._swap_elements(numbers, start_index, i)
                used.append(numbers[i])
        return permutations

    def find_permutations(self, numbers):
        return self._find_permutations_helper(numbers)


elements = [1, 2, 3]
print(Solution().find_permutations(elements))
