class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]
        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        answer = [0] * n
        tree2cnt = 0

        for i in range(m):
            bfs2 = deque([i])
            res = 0
            visit = [False] * m
            for _ in range(k):
                cur_length = len(bfs2)
                for _ in range(cur_length):
                    u = bfs2.popleft()
                    visit[u] = True
                    res += 1
                    for v in adj2[u]:
                        if not visit[v]:
                            bfs2.append(v)
            tree2cnt = max(tree2cnt, res)

        for i in range(n):
            bfs1 = deque([i])
            res = 0
            visit = [False] * n
            for _ in range(k+1):
                cur_length = len(bfs1)
                for _ in range(cur_length):
                    u = bfs1.popleft()
                    visit[u] = True
                    res += 1
                    for v in adj1[u]:
                        if not visit[v]:
                            bfs1.append(v)
            answer[i] = res + tree2cnt
        
        return answer
