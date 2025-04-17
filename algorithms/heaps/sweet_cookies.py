from bisect import insort
import heapq

class Solution:
    """
    Given a list of cookie sweetness levels, combine the least and second least
    cookies to create a new cookie of sweetness = least + 2 * second least.
    Continue to do this until all cookies are at or above the given minimum
    sweetness level.

    Return the number of combinations required to meet this
    sweetness requirement, or -1 if not possible.
    """

    # Optimized analysis: time = O(n log n), space = O(n)
    def cookiesOpt(self, k, A):
        heapq.heapify(A)
        count = 0

        while len(A) > 1 and A[0] < k:
            least = heapq.heappop(A)
            second_least = heapq.heappop(A)
            new_cookie = least + 2 * second_least
            heapq.heappush(A, new_cookie)
            count += 1

        return count if A[0] >= k else -1


    # Brute force (ish) analysis: time = O(n^2), space = O(1)
    def cookiesBF(self, k, A):
        if len(A) == 1:
            return 0 if A[0] >= k else -1

        A.sort() # n log n
        count = 0

        while A[0] < k and len(A) > 2: # n
            count += 1
            new_cookie = A[0] + A[1] * 2

            del A[0:2]  # n
            insort(A, new_cookie)  # n log n

        if A[0] >= k:
            return count
        else:
            return -1


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([1, 2, 3, 9, 10, 12], 7, 2),
        ([2, 7, 3, 6, 4, 6], 9, 4),
        ([1, 5, 6, 8, 3, 4, 5], 5, 2)
    ]

    for i, (cookies, sweetness, expected) in enumerate(test_cases, 1):
        result = s.cookiesOpt(sweetness, cookies)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
