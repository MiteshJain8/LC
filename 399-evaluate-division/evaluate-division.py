class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            pq, visit = deque([(src, 1)]), set([src])
            while pq:
                cur_node, cur_wt = pq.popleft()
                if cur_node == target:
                    return cur_wt

                for nei, wt in adj[cur_node]:
                    if nei not in visit:
                        visit.add(nei)
                        pq.append((nei, cur_wt * wt))

            return -1

        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq[0], eq[1]
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        return [bfs(a, b) for a, b in queries]