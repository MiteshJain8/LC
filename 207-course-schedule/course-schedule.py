class Solution:
    def canFinish(self, num: int, prereq: list[list[int]]) -> bool:
        can_do = [True] * num
        adj = defaultdict(list)
        req = defaultdict(set)
        for a,b in prereq:
            adj[b].append(a)
            req[a].add(b)
            can_do[a] = False
        dq = deque()
        for i in range(num):
            if can_do[i]:
                dq.append(i)
        while dq:
            course = dq.popleft()
            for c in adj[course]:
                req[c].remove(course)
                if not req[c]:
                    can_do[c] = True
                    dq.append(c)
        return False if False in can_do else True
        