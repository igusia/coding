# T: O(k*n) = O(n)
# S: O(n)
class Solution:
    def find_top_k_frequent(self, nums, k):
        if k == 0 or len(nums) <= k:
            return nums
        element_freq_map = dict()
        for num in nums:
            if num in element_freq_map.keys():
                element_freq_map[num] += 1
            else:
                element_freq_map[num] = 1
        frequency_threshold = 0
        threshold_changes = 0
        for element, freq in element_freq_map.items():
            if threshold_changes < k or freq > frequency_threshold:
                threshold_changes += 1
                frequency_threshold = freq
        elements = []
        for i in range(k):
            max_freq = 0
            max_element = 0
            for element, freq in element_freq_map.items():
                if freq >= max_freq:
                    max_freq = freq
                    max_element = element
            element_freq_map.pop(max_element)
            elements.append(max_element)
        return elements


arr = [1, 1, 1, 3, 4, 7, 2, 2, 8, 3]
k = 3
print(Solution().find_top_k_frequent(arr, k))
