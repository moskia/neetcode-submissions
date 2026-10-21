class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            adj[edge[1]].append(edge[0])

        count = 0
        visited = [False] * numCourses
        recStack = [False] * numCourses

        for i in range(numCourses):
            if not visited[i] and self.dfs(adj, i, visited, recStack, count):
                return False

        return count <= numCourses

    def dfs(self, adj, i, visited, recStack, count):

        if recStack[i]:
            return True

        if visited[i]:
            return False

        visited[i] = True
        recStack[i] = True

        # Visit all adjacent Nodes
        for j in adj[i]:
            if self.dfs(adj, j, visited, recStack, count):
                count += 1
                return True

        # Remove node from current DFS path
        recStack[i] = False

        return False
