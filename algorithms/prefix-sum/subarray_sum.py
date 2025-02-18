class Solution:
    """Returns the number of subarrays that add up to a given integer"""

    # Analysis: time = O(n), space = O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        current_sum = 0
        count = 0

        prefix_sum = {0:1}

        for ind in range(len(nums)):
            current_sum += nums[ind]
            to_find = current_sum - k

            if to_find in prefix_sum:
                count += prefix_sum[to_find]
            
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,1,1]
    assert solution.subarraySum(nums1, 2) == 2, "Test case 1 failed"

    nums2 = [1,2,3]
    assert solution.subarraySum(nums2, 3) == 2, "Test case 2 failed"

    nums3 = [1,-1,0]
    assert solution.subarraySum(nums3, 0) == 3, "Test case 3 failed"

    print("All test cases passed!")