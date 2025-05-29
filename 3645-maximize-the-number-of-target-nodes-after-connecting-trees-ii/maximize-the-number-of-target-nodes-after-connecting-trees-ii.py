class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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
        take = leave = 0

        bfs2 = deque([0])
        flag = False
        visit = [False] * m
        while bfs2:
            cur_length = len(bfs2)
            for _ in range(cur_length):
                u = bfs2.popleft()
                visit[u] = True
                if flag:
                    take += 1
                else:
                    leave += 1
                for v in adj2[u]:
                    if not visit[v]:
                        bfs2.append(v)
            flag = False if flag else True

        take = max(take, leave)
        
        color1 = [True] * n
        bfs1 = deque([0])
        ones = 0
        flag = True
        visit = [False] * n
        while bfs1:
            cur_length = len(bfs1)
            for _ in range(cur_length):
                u = bfs1.popleft()
                visit[u] = True
                if flag:
                    color1[u] = True
                    ones += 1
                else:
                    color1[u] = False
                for v in adj1[u]:
                    if not visit[v]:
                        bfs1.append(v)
            flag = False if flag else True
        
        zeroes = (n - ones) + take
        ones += take
        for i in range(n):
            answer[i] = ones if color1[i] else zeroes
        return answer