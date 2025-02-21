class Solution:
    """Finds number of subarrays with a given XOR"""

    # Analysis: time = O(n), space = O(n)
    def solve(self, nums: list[int], target:int) -> int:
        res = 0
        count_map = {0: 1}
        prefix_xor = 0

        for num in nums:
            prefix_xor ^= num

            if (prefix_xor ^ target) in count_map:
                res += count_map[prefix_xor ^ target]

            if prefix_xor in count_map:
                count_map[prefix_xor] += 1
            else:
                count_map[prefix_xor] = 1
                
        return res


if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 2, 2, 6, 4]
    target1 = 6
    assert solution.solve(nums1, target1) == 4, "Test case 1 failed"

    nums2 = [5, 6, 7, 8, 9]
    target2 = 5
    assert solution.solve(nums2 ,target2) == 2, "Test case 2 failed"

    nums3 = [1, 2, 3, 4, 5, 6, 2]
    target3 = 2
    assert solution.solve(nums3, target3) == 3, "Test case 3 failed"

    print("All test cases passed!")


