class Solution:
    """
    Return the specified element (k) between two sorted arrays.

    Note: This is the brute force approach, optimized would use binary search. 
    """

    # Analysis: time = O(n + m), space = O(1)
    # where n = len(a) and m = len(b)
    def kthElement(self, a, b, k):
        a_ptr, b_ptr, counter = 0, 0, 0
        
        while a_ptr < len(a) and b_ptr < len(b):
            if a[a_ptr] <= b[b_ptr]:
                counter += 1
                if counter == k:
                    return a[a_ptr]
                a_ptr += 1
            else:
                counter += 1
                if counter == k:
                    return b[b_ptr]
                b_ptr += 1
            
        
        while a_ptr < len(a):
            counter += 1
            if counter == k:
                return a[a_ptr]
            a_ptr += 1
        while b_ptr < len(b):
            counter += 1
            if counter == k:
                return b[b_ptr]
            b_ptr += 1
        
        # Shouldn't ever reach here, incldued for completion
        return -1 
    
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 6),
        ([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7, 256),
        ([], [1, 4, 8, 10], 3, 8)
    ]

    for i, (a, b, k, expected) in enumerate(test_cases, 1):
        output = solution.kthElement(a, b, k)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")