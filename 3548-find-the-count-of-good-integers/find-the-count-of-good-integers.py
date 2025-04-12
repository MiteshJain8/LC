class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        hset = set()
        d = (n+1)//2
        factorial = [1] * 11
        for i in range(2,11):
            factorial[i] = i * factorial[i-1]
        for num in range(10 ** (d-1), 10 ** d):
            left_half = str(num)
            s = ""
            if n & 1: 
                s = left_half + left_half[:d-1][::-1]
            else:
                s = left_half + left_half[::-1]
            number = int(s)
            if number % k != 0:
                continue
            s = ''.join(sorted(s))
            hset.add(s)
        res = 0
        for s in hset:
            count = [0] * 10
            for c in s:
                count[ord(c)-ord('0')] += 1
            non_zero = n - count[0]
            perm = non_zero * factorial[n-1]
            for val in count:
                perm //= factorial[val]
            res += perm
        return res