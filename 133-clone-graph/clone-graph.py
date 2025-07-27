"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        visit = {}
        visit[node] = Node(node.val)
        pq = deque([node])
        while pq:
            cur = pq.popleft()
            for nei in cur.neighbors:
                if nei not in visit:
                    visit[nei] = Node(nei.val)
                    pq.append(nei)
                visit[cur].neighbors.append(visit[nei])

        return visit[node]