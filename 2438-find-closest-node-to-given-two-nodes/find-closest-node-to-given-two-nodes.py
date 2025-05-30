class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        q1, q2 = deque([node1]), deque([node2])
        visited1, visited2 = set(), set()
        matching_nodes = [] # list of nodes matching the criteria. Need to return the smallest index

        while q1 or q2:
            nb_nodes_on_level1 = len(q1)
            for _ in range(nb_nodes_on_level1):
                node = q1.pop()
                visited1.add(node)
                if node in visited2:
                    matching_nodes.append(node)
                if edges[node] != -1 and edges[node] not in visited1:
                    q1.appendleft(edges[node])

            nb_nodes_on_level2 = len(q2)
            for _ in range(nb_nodes_on_level2):
                node = q2.pop()
                visited2.add(node)
                if node in visited1:
                    matching_nodes.append(node)
                if edges[node] != -1 and edges[node] not in visited2:
                    q2.appendleft(edges[node])
                
            if len(matching_nodes) > 0:
                break
        
        if len(matching_nodes)==0:
            return -1
        
        min_node = len(edges)
        for elem in matching_nodes:
            min_node = min(min_node, elem)
        return min_node