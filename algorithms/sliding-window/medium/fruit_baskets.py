from collections import defaultdict

class Solution:
    """
    Given a list of integers representing a row of trees
    where fruits[i] represents the type of fruit on the tree,
    return the total number of fruits you can collect while
    following these guidelines:
        1. You may only carry two types of fruits at once
        2. You may only pick one piece of fruit from each tree
    """

    DEBUG = False

    @staticmethod
    def _debug(*args, **kwargs):
        if Solution.DEBUG:
            print(*args, **kwargs)

    # Analysis: time = O(n), space = O(1)
    def totalFruits(self, fruits: list[int]) -> int:
        left, max_fruits = 0, 0
        fruit_count = defaultdict(int)
        Solution._debug(f"Fruit trees: {fruits}")

        for right in range(len(fruits)):
            Solution._debug(f"Picking up fruit type {fruits[right]}")
            fruit_count[fruits[right]] += 1

            while len(fruit_count) > 2:
                Solution._debug(f"Discarding fruit type {fruits[left]}")
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)
            Solution._debug(f"Max number of fruits: {max_fruits}")
            Solution._debug("---------------------")

        return max_fruits

        
if __name__ == "__main__":

    s = Solution()

    test_cases = [
        ([1, 2, 1], 3),
        ([1, 2, 3, 2, 2], 4),
        ([1, 2, 3, 4, 5, 6, 7, 8], 2)
    ]

    for i, (fruits, expected) in enumerate(test_cases, 1):
        output = s.totalFruits(fruits)
        assert output == expected, f"Optimized Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")