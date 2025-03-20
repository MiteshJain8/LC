class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def find(k):
            if parent[k] < 0:
                return k
            parent[k] = find(parent[k])
            return parent[k]

        parent = [-1] * n
        cost = [-1] * n
        for u, v, w in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                cost[pu] &= w
            elif parent[pu] < parent[pv]:
                parent[pv] = pu
                parent[pu] -= 1
                cost[pu] = cost[pv] & cost[pu] & w
            else:
                parent[pu] = pv
                parent[pv] -= 1
                cost[pv] = cost[pv] & cost[pu] & w

        res = [-1] * len(query)
        for i in range(len(query)):
            pu, pv = find(query[i][0]), find(query[i][1])
            if pu == pv:
                res[i] = cost[pu]
        return res