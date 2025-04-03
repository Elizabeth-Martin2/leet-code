from collections import defaultdict

class Solution:
    """
    Given an integer array of fish where fishes[i] represents the size
    of the fish and another integer array of bait where baits[i]
    represents the size of the bait, return how many fish can be caught
    with the given bait.

    Note: bait must strictly smaller than the fish, and each piece of
    bait may be used 3 times.
    """

    # Optimized analysis: time = O(n log n), space = O(n)
    # where n = max(len(fishes), len(baits))
    def fishBait(self, fishes: list[int], baits: list[int]) -> int:
        fish_count = 0

        fishes.sort()
        baits.sort()

        bait_count = defaultdict(int)
        f_ptr, b_ptr = 0, 0

        while f_ptr < len(fishes) and b_ptr < len(baits):
            if fishes[f_ptr] <= baits[b_ptr] or bait_count[b_ptr] >= 3:
                b_ptr += 1
            else:
                fish_count += 1
                f_ptr += 1
                bait_count[b_ptr] += 1

        return fish_count


    # Brute Force Analysis: time = O(n^2), space = O(n)
    # where n = max(len(fishes), len(baits))
    def fishBait_BF(self, fishes: list[int], baits: list[int]) -> int:
        fish_count = 0
        bait_usage = defaultdict(int)

        for f in fishes:
            for i, b in enumerate(baits):
                if b < f and bait_usage[i] < 3:
                    bait_usage[i] += 1
                    fish_count += 1
                    break

        return fish_count


if __name__ == "__main__":
    solution = Solution()


    test_cases = [
        ([5, 6], [3,4], 2),
        ([3, 4], [4, 5], 0),
        ([5, 5, 5, 5], [4], 3),
        ([7, 8, 9, 10, 11], [4, 5, 6], 5),
        ([8, 9, 10], [7, 8, 9], 3),
        ([4, 5, 6, 7], [3], 3)
    ]

    for i, (fishes, baits, expected) in enumerate(test_cases, 1):
        output = solution.fishBait(fishes, baits)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")