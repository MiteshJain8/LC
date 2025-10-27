class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        cnt = [s.count('1') for s in bank]
        res = 0
        prev = cnt[0]
        for i in range(1, m):
            if cnt[i]:
                res += (prev * cnt[i])
                prev = cnt[i]

        return res