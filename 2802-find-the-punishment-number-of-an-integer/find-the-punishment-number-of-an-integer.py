class Cache:
    def __init__(self):
        self.cache = {}
        self._precompute_values(1000)
    
    def _punishment_value(self, num: int) -> int:
        numStr = str(num * num)
        number = []
        
        def dfs(i):
            if i == len(numStr):
                val = sum(number)
                return int(numStr) if val == num else 0
            final = 0
            for j in range(i, len(numStr)):
                number.append(int(numStr[i:j+1]))
                final = max(final, dfs(j+1))
                number.pop()
            return final
            
        return dfs(0)
    
    def _precompute_values(self, n: int) -> None:
        for i in range(1, n + 1):
            value = self._punishment_value(i)
            if value > 0:
                self.cache[i] = value
    
    def get_punishment_number(self, n: int) -> int:
        return sum(self.cache.get(i, 0) for i in range(1, n + 1))


class Solution:
    _cache = Cache()
    
    def punishmentNumber(self, n: int) -> int:
        return self._cache.get_punishment_number(n)
        