class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(i):
            if i == 2*n-1:
                return True

            for num in range(n-1,0,-1):
                if num in done:
                    continue
                if num > 1 and i+num >= 2*n-1:
                    return False
                if num > 1 and res[i+num]:
                    continue
                done.add(num)
                res[i] = num
                if num > 1:
                    res[i+num] = num
                j = i+1
                while j < 2*n-1 and res[j]:
                    j += 1
                if backtrack(j):
                    return True
                done.remove(num)
                res[i] = 0
                if num > 1:
                    res[i+num] = 0
            return False

        if n == 1:
            return [1]
        res = [0] * (2*n-1)
        done = set()
        res[0], res[n] = n, n
        backtrack(1)
        return res