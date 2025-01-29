class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):
            if parent[u] < 0:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True
            if parent[pa] < parent[pb]:
                parent[pa] += parent[pb]
                parent[pb] = pa
            else:
                parent[pb] += parent[pa]
                parent[pa] = pb
            return False

        n = len(edges) + 1
        parent = [-1] * n
        for a, b in edges:
            if union(a, b):
                return [a, b]