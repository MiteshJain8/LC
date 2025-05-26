class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        dq = deque()
        node_cnt = n
        res = 0
        dp = [[0] * 26 for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1

        for u in range(n):
            if not indegree[u]:
                dq.append(u)
                dp[u][ord(colors[u]) - 97] = 1

        while dq:
            u = dq.popleft()
            node_cnt -= 1
            res = max(res, dp[u][ord(colors[u]) - 97])

            for v in adj[u]:
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i] + (ord(colors[v]) - 97 == i))
                
                indegree[v] -= 1
                if not indegree[v]:
                    dq.append(v)

        if node_cnt:
            return -1
        return res