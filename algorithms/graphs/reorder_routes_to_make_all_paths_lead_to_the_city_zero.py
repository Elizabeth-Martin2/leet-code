class Solution:
    def count_reversals_dfs(graph, visited: set, city) -> int:
        reversals = 0
        visited.add(city)

        for neighbor, direction in graph.get(city, []):
            if neighbor not in visited:
                if direction == 1:
                    reversals += 1

                reversals += Solution.count_reversals_dfs(graph, visited, neighbor)

        return reversals

    def count_reversals_bfs(graph, start_node):
        queue = deque([start_node])
        visited = set()
        reversals = 0

        while queue:
            current = queue.popleft()
            visited.add(current)

            for neighbor, direction in graph.get(current, []):
                if neighbor not in visited:
                    if direction == 1:  # Count the reversed edge
                        reversals += 1
                    queue.append(neighbor)

        return reversals
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for source, dest in connections:
            graph.setdefault(source, []).append((dest, 1))
            graph.setdefault(dest, []).append((source, 0))

        # print(graph)
        # reversals = Solution.count_reversals_bfs(graph, 0)
        visited = set()
        reversals = Solution.count_reversals_dfs(graph, visited, 0)
        return reversals