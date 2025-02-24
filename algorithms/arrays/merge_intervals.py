class Solution:
    """Analyzes a list of intervals and returns a new list with the overlapping ones merged."""
    
    # # Analysis: time = O(n log n), space = O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                if intervals[i][1] < res[-1][1]:
                    # This means intervals[i] is inside res[-1]
                    continue
                else:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        
        return res
    
if __name__ == "__main__":
    test_cases = [
        ([[1,3], [2,6], [8,10], [15,18]], [[1,6], [8,10], [15,18]]),
        ([[1,4], [4,5]], [[1,5]]),
        ([[1,4], [0,4]], [[0,4]]),
        ([[1,4], [2,3]], [[1,4]])
    ]

    solution = Solution()

    for i, (intervals, expected) in enumerate(test_cases):
        output = solution.merge(intervals)
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"
        print(f"Test case {i} passed!")

    print("All test cases passed successfully!")