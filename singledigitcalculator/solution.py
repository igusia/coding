# T: O(n) - each character only once
# S: O(n)
class Solution:
    def _calculate_subexpression(self, expression, index):
        ret = 0
        sign = 1
        i = index

        while i < len(expression):
            if expression[i] == ')':
                return ret, i
            elif expression[i] == '+':
                sign = 1
            elif expression[i] == '-':
                sign = -1
            elif expression[i] == '(':
                sub_result, new_index = self._calculate_subexpression(expression, i + 1)
                ret += sign * sub_result
                i = new_index
            else:
                ret += sign * int(expression[i])

            i += 1

        return ret, i

    def calculate(self, expression):
        ret, _ = self._calculate_subexpression(expression, 0)
        return ret


# assert single digits
print(Solution().calculate('-(3+(2-1))+5'))
