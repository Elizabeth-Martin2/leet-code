class Solution:
    """
    Given an array of book lengths (arr), assign the reading to a given number
    of students (num_students) such that the maximum number of pages assigned
    to a student is minimum.

    Uses binary search to select the number of pages
    """

    # Analysis: time = O(n log (sum(arr) - max(arr))), space = O(1)
    # where n = len(arr)
    def findPages(self, arr: list[int], num_books: int, num_students: int) -> int:
        if num_students > num_books:
            return -1

        left, right = max(arr), sum(arr)

        # Function analysis: time = O(n) where n = len(arr)
        def is_feasible(max_pages) -> bool:
            students_needed, pages_allocated = 1, 0

            for pages in arr:
                if pages_allocated + pages > max_pages:
                    students_needed += 1
                    pages_allocated = pages
                    if students_needed > num_students:
                        return False
                else:
                    pages_allocated += pages

            return True

        while left < right:
            mid = (left + right) // 2

            if is_feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
    

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([12, 34, 67, 90], 4, 2, 113),
        ([10, 20, 30, 40], 4, 2, 60),
        ([10, 20, 30, 40, 50], 5, 3, 60)
    ]

    for i, (arr, books, students, expected) in enumerate(test_cases, 1):
        output = solution.findPages(arr, books, students)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")