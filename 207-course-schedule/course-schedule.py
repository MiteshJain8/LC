class Solution:
    def canFinish(self, num: int, prereq: list[list[int]]) -> bool:
        visits = 0
        adj = defaultdict(list)
        indegree = [0] * num
        for a,b in prereq:
            adj[b].append(a)
            indegree[a] += 1
        dq = deque()
        for i in range(num):
            if indegree[i] == 0:
                dq.append(i)
                visits += 1
        while dq:
            course = dq.popleft()
            for c in adj[course]:
                indegree[c] -= 1
                if not indegree[c]:
                    visits += 1
                    dq.append(c)
        return visits == num
        