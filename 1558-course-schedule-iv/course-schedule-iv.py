class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(i):
            if dp[i]:
                return adj_set[i]

            if not adj_set[i]:
                dp[i] = True
                return set()

            cur = adj_set[i].copy()
            for j in cur:
                adj_set[i].update(dfs(j))

            dp[i] = True
            return adj_set[i]

        adj_set = [set() for _ in range(numCourses)]
        dp = [False for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_set[a].add(b)

        for i in range(numCourses):
            cur = adj_set[i].copy()
            for j in cur:
                adj_set[i].update(dfs(j))
        
        n = len(queries)
        res = [False for _ in range(n)]
        for i in range(n):
            if queries[i][1] in adj_set[queries[i][0]]:
                res[i] = True

        return res