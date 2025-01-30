class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left = longest = zeroCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
                while zeroCount > k:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
            longest = max(longest, right - left + 1)
        return longest -1
                