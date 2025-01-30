class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = longest = zeroCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
                while zeroCount > k:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
            longest = max(longest, right - left + 1) 
        return longest