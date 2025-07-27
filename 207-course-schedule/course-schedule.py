class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
            
        pq = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                pq.append(i)

        visits = 0
        while pq:
                cur = pq.popleft()
                visits += 1
                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        pq.append(nei)

        return visits == numCourses