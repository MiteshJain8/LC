class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(u, v):
            pq = deque([(u,v)])
            board[u][v] = 'S'
            while pq:
                x, y = pq.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        pq.append((nx,ny))
                        board[nx][ny] = 'S'
                        
        m = len(board)
        n = len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n-1] == 'O':
                bfs(i, n-1)
        for i in range(1,n):
            if board[0][i] == 'O':
                bfs(0, i)
            if board[m-1][i] == 'O':
                bfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'