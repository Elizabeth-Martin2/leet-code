from collections import defaultdict

class Solution:
    """
    Given number of rows and columns (m and n) of a grid, as well as the coordinates
    of black boxes in the grid, return an integer array arr of size 5 such that arr[i]
    is the number of blocks that contains exactly i black cells.

    Note: A block is defined as a 2 x 2 submatrix of the grid.

    LC. 2768 Number of Black Blocks
    """

    # Analysis: time = O(k), space = O(k)
    # where k = len(coordinates)
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        block_count = defaultdict(int)
        res = [0] * 5
        num_rows, num_cols = m, n
        
        for r, c in coordinates:
            for dr in [0, -1]:
                for dc in [0, -1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m - 1 and 0 <= nc < n - 1:
                        block_count[(nr, nc)] += 1
        
        total_blocks = (num_rows - 1) * (num_cols - 1)
        
        for count in block_count.values():
            res[count] += 1

        res[0] = total_blocks - sum(res[1:])

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (3, 3, [[0,0]], [3,1,0,0,0]),
        (3, 3, [[0,0],[1,1],[0,2]], [0,2,2,0,0])
    ]

    for i, (m, n, coordinates, expected) in enumerate(test_cases, 1):
        output = solution.countBlackBlocks(m, n, coordinates)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")