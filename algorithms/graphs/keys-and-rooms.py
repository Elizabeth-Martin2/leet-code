class Solution:
    def DFS(self, visited: dict, rooms:List[List[int]]) -> set:
        keys = deque(rooms[0])
        visited.add(0)
        while len(keys) > 0:
            key = keys.popleft()
            if key not in visited:
                visited.add(key)
                for key in rooms[key]:
                    keys.append(key)
        
        return visited
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.DFS(visited, rooms)
        # print(visited)
        return len(visited) == len(rooms)
