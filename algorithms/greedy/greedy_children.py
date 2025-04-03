from collections import defaultdict

class Solution:
    """
    Given an integer array of greed levels of children (g) and another
    integer array of cookie sizes (s), return the maximum number of
    children you can please.

    Notes: Each cookie can be given to only one child, and each child
    will only be satisfied if s[i] >= g[i].

    LC. 455 Assign Cookies
    """

    # Optimized analysis: time = O(n log n), space = O(1)
    # where n = max(len(s), len(g))
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        happy_count = 0
        g.sort()
        s.sort()

        g_ptr, s_ptr = 0, 0
        while g_ptr < len(g) and s_ptr < len(s):
            if s[s_ptr] >= g[g_ptr]:
                happy_count += 1
                g_ptr += 1  
            
            s_ptr += 1
        
        return happy_count


    # Brute force analysis: time = O(n^2), space = O(n)
    # where n = max(n, m)
    # NOTE: This BF fails large test cases with TLE
    def findContentChildren_BF(self, g: list[int], s: list[int]) -> int:
        happy_count = 0
        cookie_count = defaultdict(int)     

        g.sort()
        s.sort()

        for child in g:
            for i, c_size in enumerate(s):
                if c_size >= child and cookie_count[i] < 1:
                    happy_count += 1
                    cookie_count[i] += 1

                    break

        return happy_count


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,2,3], [1,1], 1),
        ([1,2], [1,2,3], 2),
        ([1,2,3], [3], 1)
    ]

    for i, (greed, sizes, expected) in enumerate(test_cases, 1):
        output = solution.findContentChildren_BF(greed, sizes)
        assert output == expected, f"BF Test case {i} failed, expected {expected}, got {output}"

    for i, (greed, sizes, expected) in enumerate(test_cases, 1):
        output = solution.findContentChildren(greed, sizes)
        assert output == expected, f"OPT Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")