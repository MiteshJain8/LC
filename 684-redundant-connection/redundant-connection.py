class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
                return parent[u]
            return u

        def union(a,b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True
            if rank[pb] > rank[pa]:
                parent[pa] = pb
                rank[pb] += 1
            else:
                parent[pb] = pa
                rank[pa] += 1
            return False

        n = len(edges)+1
        parent = [i for i in range(n)]
        rank = [0] * n
        for a,b in edges:
            if union(a,b):
                return [a,b]