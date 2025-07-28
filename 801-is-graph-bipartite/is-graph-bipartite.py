class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i, prev):
            if color[i]:
                if color[i] != prev:
                    return True
                return False

            color[i] = -1 * prev
            for nei in graph[i]:
                if not dfs(nei, color[i]):
                    return False
                
            return True

        n = len(graph)
        color = [0] * n
        for k in range(n):
            if not color[k] and not dfs(k, -1):
                return False
        
        return True