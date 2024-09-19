# T: O(n)
# S: O(n)
class Solution:
    def find_indices(self, numbers, target):
        if not numbers:
            return []
        value_indices = {}
        results = []
        for i in range(len(numbers)):
            number = numbers[i]
            remainder = target - number
            if remainder in value_indices.keys():
                results.append([value_indices[remainder], i])
            value_indices[number] = i
        return results


print(Solution().find_indices([2, 7, 11, 15], 18))
