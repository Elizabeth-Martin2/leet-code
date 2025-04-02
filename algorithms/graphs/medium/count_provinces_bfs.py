from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited_list = [False for _ in range(len(isConnected))]
        num_provinces = 0
        
        for i, visited in enumerate(visited_list):
            if not visited:
                num_provinces += 1
                
                to_visit = deque()
                to_visit.append(i)

                while to_visit:
                    city = to_visit.popleft()
                    visited_list[city] = True

                    for num, connection in enumerate(isConnected[city]):
                        if num == city:
                            continue
                        
                        if connection == 1 and not visited_list[num]:
                            visited_list[num] = True
                            to_visit.append(num)

        return num_provinces

