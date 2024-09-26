# T: O(n*n) = O(n^2)
# S: O(n) - depth of recursion / seen / graph
class Solution:
    def _has_cycle(self, graph, course, seen):
        if course not in graph:
            return False
        neighbors = graph[course]
        if not neighbors:
            return False
        if course in seen:
            return True
        seen.add(course)
        for neighbor in neighbors:
            if self._has_cycle(graph, neighbor, seen):
                return True
        seen.remove(course)
        return False

    def _build_graph(self, prerequisites):
        graph = {}
        for course_prerequisite in prerequisites:
            if course_prerequisite[0] in graph:
                graph[course_prerequisite[0]].append(course_prerequisite[1])
            else:
                graph[course_prerequisite[0]] = [course_prerequisite[1]]
        return graph

    def can_finish(self, prerequisites):
        if not prerequisites or len(prerequisites) <= 1:
            return True
        courses = self._build_graph(prerequisites)
        for course in courses:
            if self._has_cycle(courses, course, set()):
                return False
        return True


course_prerequisites = [[0, 1]]
print(Solution().can_finish(course_prerequisites))
course_prerequisites = [[0, 1], [1, 0]]
print(Solution().can_finish(course_prerequisites))
course_prerequisites = [[0, 3], [3, 4], [4, 0]]
print(Solution().can_finish(course_prerequisites))
course_prerequisites = [[0, 3], [3, 4], [0, 4]]
print(Solution().can_finish(course_prerequisites))
