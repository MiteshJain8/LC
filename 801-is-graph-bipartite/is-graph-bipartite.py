class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(i):
            if color[i]:
                return True

            color[i] = -1
            pq = deque([i])
            while pq:
                cur = pq.popleft()
                for nei in graph[cur]:
                    if color[nei]:
                        if color[nei] == color[cur]:
                            return False
                    else:
                        color[nei] = -1 * color[cur]
                        pq.append(nei)

            return True

        n = len(graph)
        color = [0] * n
        for k in range(n):
            if not bfs(k):
                return False
        
        return True