class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for node, pre in prerequisites:
            adj[pre].append(node)
            indegree[node] += 1

        pq = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                pq.append(i)

        visits = 0
        res = []
        while pq:
            cur = pq.popleft()
            visits += 1
            res.append(cur)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    pq.append(nei)

        return res if visits == numCourses else []