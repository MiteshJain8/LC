class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(i, sl):
            if i == n-1:
                res.append("".join(sl))
                return

            if sl[i] == '0':
                backtrack(i+1, sl+['1'])
            else:
                backtrack(i+1, sl+['1'])
                backtrack(i+1, sl+['0'])

        res = []
        backtrack(0, ['1'])
        backtrack(0, ['0'])
        return res