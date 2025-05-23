class Solution:
    """
    Given an m x n grid of characters board and a string word, 
    return true if word exists in the grid.

    LC. 79 Word Search
    """
    
    DEBUG = False
    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Overall analysis: time = O(m * n * 4^L), space = O(L)
    # where L = length of word
    def exist(self, board: list[list[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Helper function analysis: time = O(4^L) space = O(L)
        # where L = length of word
        def helper(row: int = 0, col: int = 0, ind: int = 0) -> bool:
            Solution._debug(f"Row: {row}, col: {col}, ind: {ind}")
            if ind == len(word):
                Solution._debug("Done, return true")
                return True
            if row >= num_rows or col >= num_cols or row < 0 or col < 0 or board[row][col] != word[ind]:
                Solution._debug("Out of bounds or incorrect return false")
                return False
            
            # for dr, dc in directions:
            temp = board[row][col]
            board[row][col] = "#"  # mark visited

            # explore all directions
            for dr, dc in directions:
                Solution._debug(f"Explore [{row} + {dr}, {col} + {dc}]")
                if helper(row + dr, col + dc, ind + 1):
                    return True

            board[row][col] = temp  # backtrack
            Solution._debug(f"Nothing found, return false")
            return False

        
        for r in range(num_rows):
            for c in range(num_cols):
                if helper(r, c, 0):
                    return True
        
        return False


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)
    ]

    for i, (board, word, expected) in enumerate(test_cases, 1):
        output = s.exist(board, word)
        assert output == expected, f"Test case {i} failed, expected {expected} got {output}"
    
    print("All test cases passed!")