class Solution:
    """
    Return the missing and repeated integers in an unsorted array of positive integers.

    Guaranteed: There always exists one missing and one repeating number within the range [1,n]
    """

    # Analysis: time = O(n), space = O(1)
    def findTwoElement( self,arr): 
        repeated, missing = None, None
        cs, expected_sum = 0, 0
        
        expected_sum = sum(range(1, len(arr) + 1))

        for num in arr:
            cs += abs(num)
            index = abs(num) - 1
            if arr[index] < 0:
                repeated = abs(num)
            else:
                arr[index] = -arr[index]
            
        cs -= repeated
        missing = expected_sum - cs
    
        return repeated, missing


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([6, 5, 8, 7, 1, 4, 1, 3, 2], 1, 9),
        ([2, 2], 2, 1),
        ([4, 3, 6, 2, 1, 1], 1, 5)
    ]

    for test, (nums, repeated, missing) in enumerate(test_cases):
        output = solution.findTwoElement(nums)
        assert output[0] == repeated and output[1] == missing, f"Test case {test} failed.  Expected {repeated, missing}, got {output}"

    print("All test cases passed!")
