
# Analysis: time = O(mn log n), space = O(n)
# where m = number of rows and n = number of columns
# Note: O(n) for space comes from the row sorting
def gridChallenge(grid):
    rows, cols = len(grid), len(grid[0])
       
    for row in range(rows):
        grid[row] = sorted(grid[row])

    
    for c in range(0, cols):
        temp = ord(grid[0][c])
        
        for r in range(1, rows):
            if ord(grid[r][c]) < temp:
                return "NO"
            
            temp = ord(grid[r][c])
        
    return "YES"

if __name__ == "__main__":
    test_cases = [
        (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),
        (["abc", "lmp", "qrt"], "YES"),
        (["mpxz", "abcd", "wlmf"], "NO"),
        (["abc", "hjk", "mpq", "rtv"], "YES"),
        (["zxy", "wvu", "tsr"], "NO")
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        output = gridChallenge(grid[:])
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")
