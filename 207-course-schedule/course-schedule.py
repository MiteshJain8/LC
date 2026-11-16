class Solution:
    def canFinish(self, num: int, prereq: list[list[int]]) -> bool:
        def dfs(src):
            if visited[src]:
                return False
            if adj[src] == []:
                return True
            visited[src] = True
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            visited[src] = False
            adj[src] = []
            return True

        adj = defaultdict(list)
        visited = [False] * num
        for a,b in prereq:
            adj[b].append(a)
        for i in range(num):
            if not dfs(i):
                return False
        return True
        