def multiplicate(A,B):
    n = len(A)
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k]*B[k][j]
            res[i][j] =  res[i][j] % (10**9+7)
    return res

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        @cache
        def mpower(t):
            if t == 1:return mat
            if t % 2 == 1:
                res = multiplicate(mat,mpower(t-1))
            elif t // 2 > 0:
                res=multiplicate(mpower(t//2),mpower(t//2))
            return res

        freq = [0]*26
        for a in s:
            freq[ord(a)-ord('a')] += 1
        mat = [[0 for i in range(26)] for j in range(26)]
        for i,a in enumerate(nums):
            for q in range(1,a+1):
                mat[i][(q+i)%26] += 1
                
        M = mpower(t)
        res = 0
        for i in range(26):
            res += sum([freq[j]*M[j][i] for j in range(26)])
        return res % (10**9+7)
        