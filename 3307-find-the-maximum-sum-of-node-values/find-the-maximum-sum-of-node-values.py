class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    

    def find(self, x):
        cur = x
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        
        if self.rank[pa] >= self.rank[pb]:
            self.par[pb] = pa
            if self.rank[pa] == self.rank[pb]:
                self.rank[pa] += 1
        else:
            self.par[pa] = pb
        return True


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        uf = UF(n)
        diff = list()
        for i in range(n):
            diff.append((nums[i] ^ k) - nums[i])
        for u, v in edges:
            uf.union(u, v)
        
        root_heap = dict()
        for i in range(n):
            root = uf.find(i)
            if root not in root_heap:
                root_heap[root] = [-diff[i]]
            else:
                root_heap[root].append(-diff[i])
        
        for root in root_heap:
            heapify(root_heap[root])
        
        delta = 0
        for rh in root_heap.values():
            if rh: x1 = heappop(rh)
            else: continue
            if rh: x2 = heappop(rh)
            else: continue
            while (-x1) + (-x2) > 0:
                delta += (-x1) + (-x2)
                if rh: x1 = heappop(rh)
                else: break
                if rh: x2 = heappop(rh)
                else: break
        
        return sum(nums) + delta