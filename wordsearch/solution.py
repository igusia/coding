# T: O(n^2)
# S: O(1)
class Solution:
    def find_word(self, w, m):
        for row in m:
            for i in range(len(row)):
                if row[i] != w[i]:
                    break
                if i == len(row) - 1:
                    return True
        for i in range(len(m)):
            for j in range(len(m)):
                if m[j][i] != w[j]:
                    break
                if j == len(m) - 1:
                    return True
        return False


matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
word = 'FOAM'
print(Solution().find_word(word, matrix))
