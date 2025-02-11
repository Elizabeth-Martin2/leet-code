class Solution:
    """Find two integers that add up to the target sum"""

    # Analysis: time = O(n), space = O(n) 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Returns a list of two indices that add up to the target sum.

        Assumptions provided: each input has exactly one solution,
        and elements may be used only once
        """
        prefix_sum = {} # O(n) space

        for i, num in enumerate(nums): # O(n) time
            solution = target - num
            if solution in prefix_sum:
                if prefix_sum[solution] != i:
                    return i, prefix_sum[solution]
            
            prefix_sum[num] = i

        return -1

if __name__ == "__main__":
    nums1 = [2,7,11,15]
    target1 = 9
    sol1 = Solution().twoSum(nums1, target1)
    print(f"Nums1: {nums1}, target1: {target1}")
    print(f"Indices: {sol1[0]} = {nums1[sol1[0]]} + {sol1[1]} = {nums1[sol1[1]]} = {target1}")
    print("-------------------")

    nums2 = [3,2,4]
    target2 = 6
    sol2 = Solution().twoSum(nums2, target2)
    print(f"Nums2: {nums2}, target2: {target2}")
    print(f"Indices: {sol2[0]} = {nums2[sol2[0]]} + {sol2[1]} = {nums2[sol2[1]]} = {target2}")
    print("-------------------")

    nums3 = [3,3]
    target3 = 6
    sol3 = Solution().twoSum(nums3, target3)
    print(f"Nums3: {nums3}, target3: {target3}")
    print(f"Indices: {sol3[0]} = {nums3[sol3[0]]} + {sol3[1]} = {nums3[sol3[1]]} = {target3}")