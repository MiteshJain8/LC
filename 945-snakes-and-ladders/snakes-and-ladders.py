class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        map_idx = {}
        flag = True
        k = 1
        for i in range(n-1, -1, -1):
            if flag:
                flag = False
                for j in range(n):
                    map_idx[k] = (i,j)
                    k += 1
            else:
                flag = True
                for j in range(n-1, -1, -1):
                    map_idx[k] = (i,j)
                    k += 1

        dq = deque([(1, 0)]) # [square, moves]
        visit = set()
        while dq:
            sq, moves = dq.popleft()

            for i in range(1,7):
                nxtSq = sq + i
                r,c = map_idx[nxtSq]
                if board[r][c] != -1:
                    nxtSq = board[r][c]
                if nxtSq == n * n:
                    return moves + 1
                if nxtSq not in visit:
                    visit.add(nxtSq)
                    dq.append((nxtSq, moves+1))
        return -1
                    