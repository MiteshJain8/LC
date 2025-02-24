class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        bob_parent = {}
        
        def find_path_to_root(u, p):
            if u == 0:
                return True
            for v in adj[u]:
                if v != p:
                    if find_path_to_root(v, u):
                        bob_parent[u] = v
                        return True
            return False
            
        find_path_to_root(bob, -1)

        def dfs(a, b, alice_parent):
            bob_amount = amount[b]
            alice_amount = 0
            if a == b:
                alice_amount = (amount[a] // 2)
            else:
                alice_amount = amount[a]
            
            if len(adj[a]) == 1 and adj[a][0] == alice_parent:
                return alice_amount

            amount[b] = 0
            nxt_b = bob_parent.get(b, 0)

            mx = float('-inf')
            for nxt_a in adj[a]:
                if nxt_a != alice_parent:
                    mx = max(mx, alice_amount + dfs(nxt_a, nxt_b, a))

            amount[b] = bob_amount
            return mx
        
        return dfs(0, bob, -1)