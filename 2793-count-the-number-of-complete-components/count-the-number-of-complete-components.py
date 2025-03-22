class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(k):
            if parent[k] < 0:
                return k
            parent[k] = find(parent[k])
            return parent[k]

        parent = [-1] * n
        edge_count = [0] * n
        components = n

        for a,b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                edge_count[pa] += 1
                continue
            if parent[pa] < parent[pb]:
                parent[pa] += parent[pb]
                parent[pb] = pa
                edge_count[pa] += (1 + edge_count[pb])
            else:
                parent[pb] += parent[pa]
                parent[pa] = pb
                edge_count[pb] += (1 + edge_count[pa])
            components -= 1

        for i in range(n):
            node_cnt = -parent[i]
            if node_cnt > 0 and edge_count[i] != node_cnt*(node_cnt-1)/2:
                components -= 1
                
        return components