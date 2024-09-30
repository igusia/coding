class Intersection:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = start + end // 2

    def get_right(self):
        return self.end

    def get_left(self):
        return self.start

    def get_mid(self):
        return self.mid


class Domino:
    def __init__(self, index, state):
        self.index = index
        self.state = state


# T: O(nlogn) - sort
# S: O(n)
class Solution:
    def _find_intersections(self, right, left, size):
        points = sorted(right + left)
        intersections = [Intersection(0, points[0])]
        intersections.extend([Intersection(points[i], points[i + 1]) for i in range(len(points) - 1)])
        intersections.extend([Intersection(points[len(points) - 1], size)])
        return intersections

    def resolve_dominoes_state(self, right, left, size):
        if size < 1:
            return {}
        intersections = self._find_intersections(right, left, size)
        dominoes = {}
        for intersection in intersections:
            if intersection.get_left() in left:
                dominoes[intersection.get_left()] = -1
                for domino_index in range(intersection.get_left() + 1, intersection.get_right()):
                    dominoes[domino_index] = -1 if intersection.get_right() in left else 0
            elif intersection.get_left() in right:
                if intersection.get_right() in left:
                    if (intersection.get_right() + intersection.get_left()) % 2 == 0:
                        dominoes[intersection.get_mid()] = 0
                    for domino_index in range(intersection.get_left(), intersection.get_mid()):
                        dominoes[domino_index] = 1
                        dominoes[intersection.get_right() + intersection.get_left() - domino_index] = -1
                else:
                    for domino_index in range(intersection.get_left(), intersection.get_right()):
                        dominoes[domino_index] = 1
            else:
                for domino_index in range(intersection.get_left(), intersection.get_right()):
                    dominoes[domino_index] = -1 if intersection.get_right() in left else 0
        return dominoes


dominoes_right = [2, 9]
dominoes_left = [6]
dominoes_size = 11
result = Solution().resolve_dominoes_state(dominoes_right, dominoes_left, dominoes_size)
print([result[i] for i in range(dominoes_size)])
# | | / / | \ \ | | / /
# 0 0 1 1 0 -1 -1 0 0 1 1
