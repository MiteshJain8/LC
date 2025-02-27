class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hset = set(arr)
        res, n = 0, len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                cur, prev = arr[j], arr[i]
                length, nxt = 2, cur+prev
                while nxt in hset:
                    length += 1
                    res = max(res, length)
                    cur, prev = nxt, cur
                    nxt = cur+prev
        return res
