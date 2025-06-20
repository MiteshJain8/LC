class Solution:
    def maxDistance(self, st: str, k: int) -> int:
        def getBest(vals):
            cur = 0
            used = 0
            res = 0
            for v in vals:
                if v < 0 and used < k:
                    used += 1
                    cur += 1
                else:
                    cur += v
                res = max(res, cur)
            return res

        t1 = {'N':1,'S':-1,'E':1,'W':-1}
        t2 = {'N':-1,'S':1,'E':1,'W':-1}
        t3 = {'N':1,'S':-1,'E':-1,'W':1}
        t4 = {'N':-1,'S':1,'E':-1,'W':1}
        arr1 = [t1[c] for c in st]
        arr2 = [t2[c] for c in st]
        arr3 = [t3[c] for c in st]
        arr4 = [t4[c] for c in st]
        return max(getBest(arr1), getBest(arr2), getBest(arr3), getBest(arr4))