class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu < pv:
                parent[pv] = pu
            else:
                parent[pu] = pv

        n = len(baseStr)
        parent = [i for i in range(26)]
        for a,b in zip(s1,s2):
            if a == b:
                continue
            union(ord(a)-97, ord(b)-97)

        res = [''] * n
        for i in range(n):
            res[i] = chr(find(ord(baseStr[i])-97) + 97)

        return "".join(res)