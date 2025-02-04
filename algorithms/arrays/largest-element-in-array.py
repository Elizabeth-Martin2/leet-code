class solution:
    """Returns largest integer from an array"""

    # Analysis: O(n)
    def largest(self, arr: list[int]) -> int:
        return max(arr)

if __name__ == "__main__":
    arr = [1, 8, 7, 56, 90]
    print(f"Array: {arr}")

    largest = solution().largest(arr)
    print(f"Largest number: {largest}")
