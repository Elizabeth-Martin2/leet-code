class Solution:
    """Finds the longest subarray that sum to a given target."""
    
    # Analysis: time = O(n), space = O(n) where n = len(arr)
    def longest_subarray(self, arr: list[int], k: int) -> int:
        """Returns the length of the longest subarray in arr that sum to k"""
        prefix_sum = {0: -1}
        max_len = current_sum = 0
        
        for i, num in enumerate(arr):
            current_sum += num
            
            if current_sum - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[current_sum - k])
            
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
            
        return max_len

if __name__ == "__main__":
    nums1 = [94, -33, -13, 40, -82, 94, -33, -13, 40, -82]
    k1 = 52
    print(f"Nums1: {nums1}, k = {k1}, longest subarray: {Solution().longest_subarray(nums1, k1)}")

    nums2 = [10, 6, 1, 2, 4, 1, 2, -10]
    k2 = 16
    print(f"Nums2: {nums2}, k = {k2}, longest subarray: {Solution().longest_subarray(nums2, k2)}")