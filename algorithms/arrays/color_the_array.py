class Solution:
    """
    Given a length (n) to represent a line of colored nodes (initially uncolored)
    and an array of queries structured like [coord, color], perform each query
    then record the number of adjacent neighbors with similar colors.  Return the
    array of tracked neighbors.

    LC. 2672 Number of Adjacent Elements With the Same Color
    """

    # Analysis: time = O(q), space = O(q + n)
    # where q = len(queries)
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        res = [0 for _ in range(len(queries))]
        colors = [0 for _ in range(n)]

        neighbors = 0
        
        for i, (coord, color) in enumerate(queries):
            if colors[coord] != 0:
                if coord > 0 and colors[coord] == colors[coord - 1]:
                    neighbors -= 1
                if coord < len(colors) - 1 and colors[coord] == colors[coord + 1]:
                    neighbors -= 1
                    
            colors[coord] = color
            
            if coord > 0 and colors[coord] == colors[coord - 1]:
                neighbors += 1
            if coord < len(colors) - 1 and colors[coord] == colors[coord + 1]:
                neighbors += 1
            
            res[i] = neighbors

        return res


if __name__ == "__main__":
    solution = Solution()


    test_cases = [
        (4, [[0,2],[1,2],[3,1],[1,1],[2,1]], [0,1,1,0,2]),
        (1, [[0,100000]], [0]),
        (15, [[10,2],[12,1],[7,1],[11,1],[5,3],[14,3],[12,2],[14,3],[3,2],[13,3],[11,1],[2,2],[2,1],[4,2]], [0,0,0,1,1,1,0,0,0,1,1,2,1,2])
    ]

    for i, (n, queries, expected) in enumerate(test_cases, 1):
        output = solution.colorTheArray(n, queries)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")