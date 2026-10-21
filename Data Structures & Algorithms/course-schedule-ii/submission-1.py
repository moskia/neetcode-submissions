class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        visited = [False] * numCourses
        recStack = [False] * numCourses
        courses = []

        for u in range(numCourses):
            if not visited[u] and self.dfs(graph, u, visited, recStack, courses):
                return []
        print(courses)
        courses.reverse()
        return courses


    def dfs(self, graph, u, visited, recStack, courses):
        
        if recStack[u]:
            return True

        if visited[u]: 
            return False

        recStack[u] = True
        visited[u] = True

        for v in graph[u]:
            if self.dfs(graph, v, visited, recStack, courses):
                return True

        courses.append(u)
        recStack[u] = False

        return False

