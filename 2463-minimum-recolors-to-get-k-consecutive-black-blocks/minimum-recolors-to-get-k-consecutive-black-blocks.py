class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dq = deque()
        n = res = len(blocks)
        l = cur = 0
        for r in range(n):
            if blocks[r] == 'W':
                dq.append(r)
                cur += 1
            while r-l+1 >= k:
                res = min(res, cur)
                if dq:
                    j = dq.popleft()
                    l = j + 1
                    cur -= 1
                else:
                    break
        return res