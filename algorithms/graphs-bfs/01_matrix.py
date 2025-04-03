from collections import deque

class Solution:
    """
    Given an m x n binary matrix mat, return the distance of the
    nearest 0 for each cell.

    Uses Breadth first search

    LC. 542 01 Matrix
    """

    # Analysis: time = O(n * m), space = O(n * m)
    # where n = num rows and m = num cols
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        tbd = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    tbd.append((r,c))
                else:
                    mat[r][c] = -1
        

        directions = [[0,-1], [0,1], [1,0], [-1,0]]
        dist = 1
        while tbd:
            for _ in range(len(tbd)):
                r, c = tbd.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= rows:
                        continue
                    if nc < 0 or nc >= cols:
                        continue
                    
                    if mat[nr][nc] == -1 or mat[nr][nc] > dist:
                        mat[nr][nc] = dist
                        tbd.append((nr, nc))
            
            dist += 1
        
        return mat

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [[0, 1],  [1, 1]], [[0, 1], [1, 2]]
        ),
        (
            [[0, 0], [0, 0]], [[0, 0], [0, 0]]
        ),
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        ),
        (
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[0, 1, 0], [1, 2, 1], [0, 1, 0]]
        ),
        (
            [[1, 1, 1], [0, 0, 0], [1, 1, 1]], [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
        )
    ]

    for i, (mat, expected) in enumerate(test_cases, 1):
        result = solution.updateMatrix([row[:] for row in mat])
        assert result == expected, f"Test case {i} failed:\nExpected: {expected}\nGot: {result}"

    print("All test cases passed!")
