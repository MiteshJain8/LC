class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        components = []
        vertices = {}
        
        def dfs(vertex, component_idx):
            visited.add(vertex)
            vertices[vertex] = component_idx
            components[component_idx].add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, component_idx)

        for vertex in range(1, c + 1):
            if vertex not in visited:
                components.append(SortedSet())
                dfs(vertex, len(components) - 1)

        res = []
        for op, vertex in queries:
            component = components[vertices[vertex]]
            if op == 1:
                if vertex in component:
                    res.append(vertex)
                elif len(component) > 0:
                    res.append(component[0])
                else:
                    res.append(-1)
            else:
                if vertex in component:
                    component.remove(vertex)
        return res