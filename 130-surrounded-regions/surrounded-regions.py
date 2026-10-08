class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_dfs(a, b):
            if a == m or b == n or a == 0 or b == 0:
                return False

            check[a][b] = True
            res = True
            for dx, dy in sides:
                x, y = a + dx, b + dy
                if 0 <= x <= m and 0 <= y <= n and board[x][y] == "O" and not check[x][y]:
                    cur = check_dfs(x, y)
                    res = res and cur
                    # print(x, y, cur)
            return res

        def mark_dfs(a, b):
            board[a][b] = "X"
            for dx, dy in sides:
                x, y = a + dx, b + dy
                if 0 < x < m and 0 < y < n and board[x][y] == "O":
                    mark_dfs(x, y)
            return
            
        m, n = len(board)-1, len(board[0])-1
        check = [[False] * (n+1) for _ in range(m+1)]
        sides = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O" and not check[i][j]:
                    if check_dfs(i, j):
                        mark_dfs(i, j)