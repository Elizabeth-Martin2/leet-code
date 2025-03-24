class Solution:
    """
    Returns the minimum number of days required to wait to be able to make
    a given number (m) of bouquets each with a given number (k) of adjacent
    flowers depending days the flowers bloom (bloomDays).

    Uses binary search to find the minimum number of days.

    LC 1482. Minimum number of days to make m Bouquets
    """

    # Analysis: time = O(n log (max(bloomDay) - min(bloomDay))), space = O(1)
    # where m = number of required bouquets and n = len(bloomDay)
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        num_reqd_bouquets, flowers_per_bouquet = m, k

        # Base case / early exit
        if len(bloomDay) < num_reqd_bouquets * flowers_per_bouquet:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            bouquets, flowers = 0, 0
            for pot in bloomDay:
                if pot <= mid:
                    flowers += 1
                else:
                    flowers = 0 # they need to be adj.
                
                if flowers == flowers_per_bouquet:
                    bouquets += 1
                    flowers = 0 # reset counter
            
            if bouquets >= num_reqd_bouquets:
                # maybe we could have waited less days
                right = mid
            else:
                # maybe we need to wait longer
                left = mid + 1
        
        return right

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([7,7,7,7,12,7,7], 2, 3, 12),
        ([1,10,3,10,2], 3, 2, -1),
        ([1,10,3,10,2], 3, 1, 3)
    ]

    for i, (bloomDay, num_reqd_bouquets, flowers_per_bouquet, expected) in enumerate(test_cases, 1):
        output = solution.minDays(bloomDay, num_reqd_bouquets, flowers_per_bouquet)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")