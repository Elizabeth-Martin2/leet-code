class Solution:
    def provinceDFS(self, connections: List[int], isConnected: List[List[int]], visited: set):
        for i, connection in enumerate(connections):
            if connection == 1 and i not in visited:
                visited.add(i)
                self.provinceDFS(isConnected[i], isConnected, visited)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0        
        visited = set()
        
        for cityNum in range(len(isConnected[0])):  # O(n)
            if cityNum not in visited:
                visited.add(cityNum)
                self.provinceDFS(isConnected[cityNum], isConnected, visited)    # O(n)
                provinces += 1

        return provinces    # resulting complexity: O(n^2)