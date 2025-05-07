class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        n, m = len(moveTime), len(moveTime[0])
        dirs = [0, -1, 0, 1, 0]
        moveTime[0][0] = -1
        while pq:
            t, r, c = heappop(pq)
            if r == n-1 and c == m-1:
                return t

            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i+1]
                if 0 <= nr < n and 0 <= nc < m and moveTime[nr][nc] != -1:
                    heappush(pq, (max(t+1, moveTime[nr][nc]+1), nr, nc))
                    moveTime[nr][nc] = -1
        return -1