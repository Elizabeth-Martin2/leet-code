from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    """
    Given a sorted doubly linked list of size 'n', consisting of distinct
    positive integers, and a number 'k', return the pairs of integers that
    sum to k.

    Note: Expected time complexity is O(n)
    Coding ninjas: https://www.naukri.com/code360/problems/find-pair-with-a-given-sum-in-a-doubly-linked-list_1164172
    """

    # Optimized two pointer approach
    # Analysis: time = O(n), space = O(n) [for ouptut res, otherwise O(1) space]
    # where n = number of nodes in linked list
    def findPairs(self, head: Optional[ListNode], k: int) -> list[list[int]]:
        res = []
        left = right = head

        # Go to tail of linked list
        while right.next:
            right = right.next

        while left.val < right.val:
            current_sum = left.val + right.val

            if current_sum == k:
                res.append([left.val, right.val])
                left = left.next
                right = right.prev

            elif current_sum < k:
                left = left.next
            else:
                right = right.prev

        return res


    # Brute force (ish) approach
    # Analysis: time = O(n), space = O(n)
    # where n = number of nodes in linked list
    def findPairsBF(self, head: Optional[ListNode], k: int) -> list[list[int]]:
        prefix_sum = set()
        node = head
        res = []

        while node:
            to_find = k - node.val
            if to_find in prefix_sum:
                res.append([node.val, to_find])

            if node.val not in prefix_sum:
                prefix_sum.add(node.val)

            node = node.next

        return res


# Helper functions for testing
def list_to_doubly_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    prev = head
    for val in arr[1:]:
        node = ListNode(val)
        prev.next = node
        node.prev = prev
        prev = node
    return head

def doubly_linkedlist_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([1, 2, 3, 4], 5, [[1, 4], [2, 3]]),
        ([1, 2, 3, 4, 6], 7, [[1, 6], [3, 4]]),
        ([1, 2, 9], 12, [])
    ]

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        dll = list_to_doubly_linkedlist(arr)
        output = s.findPairs(dll, target)
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")