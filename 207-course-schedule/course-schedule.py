class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(src):
            if src in visit:
                return False

            if adj[src] == []:
                return True

            visit.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            visit.remove(src)
            adj[src] = []

            return True

        adj = defaultdict(list)
        visit = set()
        for node, pre in prerequisites:
            adj[pre].append(node)

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True