class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [False] * (right+1)
        sieve[0] = sieve[1] = True
        primes, res = [], [-1, -1]
        diff = right
        for i in range(2,right+1):
            if not sieve[i]:
                if i >= left:
                    if primes:
                        if i-primes[-1] <= 2:
                            return [primes[-1], i]
                        elif i-primes[-1] < diff:
                            diff = i-primes[-1]
                            res = [primes[-1], i]
                    primes.append(i)
                j = i
                while j <= right:
                    sieve[j] = True
                    j += i
        return res
