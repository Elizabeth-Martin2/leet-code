class Solution: 
    """
    Given a 2n x 2n matrix where every cell has an integer,
    you may reverse any of the rows or columns any number
    of times. The goal is to maximize the sum of the elements
    in the n x n submatrix in the upper-left quadrant of the
    matrix.
    """

    # Analysis: time = O(n^2), space = O(1)
    # where n = len(matrix) // 2
    def flippingMatrix(self, matrix):
        n = len(matrix) // 2
        total = 0

        for i in range(n):
            for j in range(n):
                total += max(
                    matrix[i][j],
                    matrix[i][2*n - 1 - j],
                    matrix[2*n - 1 - i][j],
                    matrix[2*n - 1 - i][2*n - 1 - j]
                )

        return total


if __name__ == "__main__":
    s = Solution()

    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert s.flippingMatrix(matrix) == 4

    matrix = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108]
    ]
    assert s.flippingMatrix(matrix) == 414

    matrix = [
        [5, 5],
        [5, 5]
    ]
    assert s.flippingMatrix(matrix) == 5

    matrix = [
        [4096, 1],
        [1, 4096]
    ]
    assert s.flippingMatrix(matrix) == 4096

    matrix = [
        [1, 2, 100, 101],
        [3, 4, 102, 103],
        [200, 201, 5, 6],
        [202, 203, 7, 8]
    ]
    assert s.flippingMatrix(matrix) == 203 + 202 + 201 + 200

    print("All test cases passed!")
