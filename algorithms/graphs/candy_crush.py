from typing import List

# TODO: Come back and review this one

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])
        changed = True

        while changed:
            changed = False
            # Step 1: Mark horizontal candies
            for r in range(rows):
                for c in range(cols - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c+1]) and val == abs(board[r][c+2]):
                        board[r][c] = -val
                        board[r][c+1] = -val
                        board[r][c+2] = -val
                        changed = True

            # Step 2: Mark vertical candies
            for c in range(cols):
                for r in range(rows - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r+1][c]) and val == abs(board[r+2][c]):
                        board[r][c] = -val
                        board[r+1][c] = -val
                        board[r+2][c] = -val
                        changed = True

            # Step 3: Apply gravity
            for c in range(cols):
                wr = rows - 1  # write row pointer
                for r in range(rows - 1, -1, -1):
                    if board[r][c] > 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for r in range(wr, -1, -1):
                    board[r][c] = 0

        return board


if __name__ == "__main__":
    board = [
    [110,   5,      112,    113,    114],
    [210,   211,    5,      213,    214],
    [310,   311,    3,      313,    314],
    [410,   411,    412,    5,      414],
    [5,     1,      512,    3,      3],
    [610,   4,      1,      613,    614],
    [710,   1,      2,      713,    714],
    [810,   1,      2,      1,      1],
    [1,     1,      2,      2,      2],
    [4,     1,      4,      4,      1014]
    ]

    solution = Solution()
    stable_board = solution.candyCrush(board)

    for row in stable_board:
        print(row)
