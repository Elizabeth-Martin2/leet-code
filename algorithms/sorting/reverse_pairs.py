class Solution:
    """
    Returns the number of reverse pairs in an array by using merge sort.

    A reverse pair is a pair (i, j) where
      0 <= i < j < nums.length and
      nums[i] > 2 * nums[j].
    """

    # Merge function analysis: time = O(n), space = O(n)
    def merge(self, nums: list[int], left:int = 0, mid:int = 0, right:int = 0) -> int:
        count = 0
        j = mid + 1
        
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2* nums[j]:
                j += 1
            count += (j - (mid + 1))
        
        # Use a temp array to preserve ordering while counting reverse pairs
        # This bring space complexity up to O(n) where it'd normally be O(1)
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1

        nums[left:right + 1] = temp
        return count
    
    # Overall Analysis: time = O(n log n), space = O(n)
    def reversePairs(self, nums: list[int], left:int = 0, right:int = None) -> int:
        if right == None:
            right = len(nums) - 1

        if left < right:
            mid = (left + right) // 2

            left_count = self.reversePairs(nums, left, mid)
            right_count = self.reversePairs(nums, mid + 1, right)
            merge_count = self.merge(nums, left, mid, right)

            return left_count + right_count + merge_count
        
        return 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1,3,2,3,1], 2),
        ([2,4,3,5,1], 3),
        ([10,9,8,7,6,5,4,3,2,1], 20)
    ]

    for i, (test, expected) in enumerate(test_cases):
        output = solution.reversePairs(test)
        assert output == expected, f"Test case {i + 1} failed, expected {expected}, got {output}"

    print("All test cases passed!")