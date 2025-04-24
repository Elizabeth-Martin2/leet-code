from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a sorted linked list, delete all nodes that
    have duplicate numbers, leaving only distinct numbers from the
    original list. Return the linked list sorted as well.

    LC. 82 Remove Duplicates from Sorted List 2
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in linked list
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            has_duplicate = False

            while current.next and current.val == current.next.val:
                has_duplicate = True
                current = current.next

            if has_duplicate:
                current = current.next
                # continue skips below lines for this iteration
                # so that prev is updated to the next distinct number
                continue

            prev.next = current
            prev = current
            current = current.next

        prev.next = None
        return dummy.next


# helper functions
def list_to_linkedlist(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    if not head:
        return None
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([0, 1, 2, 2, 3, 3, 4], [0, 1, 4]),
        ([1, 1, 1, 2, 2], None),
        ([9, 9, 9, 10], [10])
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        l1 = list_to_linkedlist(arr)
        output = s.deleteDuplicates(l1)
        result = linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
