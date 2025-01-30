class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bipartite_bfs(i):
            comp = [i]
            colors[i] = 1
            color = 1
            q = deque([i])
            while q:
                color = 1-color
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if colors[nei] == -1:
                            colors[nei] = color
                            q.append(nei)
                            comp.append(nei)
                        elif colors[nei] == colors[cur]:
                            return -1, []
            return 0, comp

        def bfs(j):
            q = deque([j])
            visit = [False] * (n+1)
            visit[j] = True
            lvl = 0
            while q:
                lvl += 1
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if not visit[nei]:
                            q.append(nei)
                            visit[nei] = True
            return lvl

        adj = [[] for _ in range(n+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0
        colors = [-1] * (n+1) 
        for i in range(1,n+1):
            if colors[i] != -1:
                continue
            max_cnt, component = bipartite_bfs(i)
            if max_cnt == -1:
                return -1
            print(component)
            for j in component:
                max_cnt = max(max_cnt, bfs(j))
            res += max_cnt
        return res
