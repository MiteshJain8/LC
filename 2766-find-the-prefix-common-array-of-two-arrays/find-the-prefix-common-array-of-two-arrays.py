class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seta, setb = set(), set()
        cnt, res, i = 0, [0] * len(A), 0
        for a,b in zip(A,B):
            seta.add(a)
            setb.add(b)
            if a != b and a in setb and b in seta:
                cnt += 2
            elif a == b:
                cnt += 1
            elif a in setb or b in seta:
                cnt += 1
            res[i] = cnt
            i += 1
        return res