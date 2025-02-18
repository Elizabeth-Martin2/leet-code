class Solution:
    """Returns the requested number of rows of pascal's triangle in the form of a list of lists of integers"""

    # Analysis: time = O(n^2), space = O(n^2) where n = num_rows
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for current_row in range(1, numRows):
            new_res_row = [1]

            for i in range(1, current_row):
                new_res_row.append(res[-1][i] + res[-1][i - 1])

            new_res_row.append(1)
            res.append(new_res_row)
        
        return res


if __name__ == "__main__":
    solution = Solution()

    num_rows = 7
    output = solution.generate(7)

    res = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1]]
    for row in range(num_rows):
        # print(output[row])
        assert output[row] == res[row], f"Test case failed on row {row}"

    print("All test cases passed!")