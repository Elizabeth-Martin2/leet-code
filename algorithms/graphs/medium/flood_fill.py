from collections import deque
class Solution:
    """
    Implement the flood fill approach.  Given an image matrix of integers (image), a source row (sr),
    a source column (sc) and a color integer (color), change all neighboring pixels of the source row
    and column to the given color.

    LC. 733 Flood Fill
    """

    # Analysis: time = O(m * n), space = O(1)
    # where m = number of rows, and n = number of columns
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        key = image[sr][sc]
        if key == color:
            return image
        
        num_rows, num_cols = len(image), len(image[0])
        directions = [(-1, 0), (1,0), (0,-1), (0, 1)]

        to_visit = deque()
        to_visit.append([sr,sc])

        while to_visit:
            pixel_row, pixel_col = to_visit.popleft()

            image[pixel_row][pixel_col] = color            
            
            for delta_row, delta_col in directions:
                next_row, next_col = pixel_row + delta_row, pixel_col + delta_col

                if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                    if image[next_row][next_col] == key:
                        to_visit.append([next_row, next_col])

        return image

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),
        ([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]]),
        ([[1]], 0, 0, 0, [[0]])
    ]

    for i, (image, sr, sc, color, expected) in enumerate(test_cases, 1):
        output = solution.floodFill(image, sr, sc, color)

        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")