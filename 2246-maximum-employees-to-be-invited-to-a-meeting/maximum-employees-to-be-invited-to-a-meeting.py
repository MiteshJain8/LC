class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)

        levels, graph, indegree = [1]*n, defaultdict(list), [0]*n

        for i in range(n):
            indegree[favorite[i]] += 1 
            graph[i].append(favorite[i])

        stack = []

        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            node = stack.pop(0) 

            for neighbor in graph[node]:
                indegree[neighbor] -= 1 
                levels[neighbor] = levels[node] + 1 
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        cyclic_nodes = {i for i in range(n) if indegree[i] != 0}

        longest_path, answer = 0, [-1]*n

        for i in cyclic_nodes:
            if answer[i] == -1:
                stack, visited = [i], {i}

                while stack:
                    c_node = stack.pop()

                    for neighbor in graph[c_node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)

                for j in visited:
                    answer[j] = len(visited)

                if len(visited) == 2:
                    for j in visited:
                        longest_path += levels[j]

        return max(longest_path,max(answer))