# T: O(nlogn)
# S: O(n)
class Solution:
    def reconstruct(self, heights):
        heights.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for height in heights:
            position = height[1]
            result.insert(position, height)
        return result


arr = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstruct(arr))
