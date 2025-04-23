from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    """
    Given the head of a doubly linked list and an integer target.
    Delete all nodes in the linked list with the value target and
    return the head of the modified linked list.
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in linked list
    def deleteAllOccurrences(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        dummy = ListNode(0, head, None)
        node, prev = dummy.next, dummy

        while node:
            if node.val == target:
                prev.next = node.next
                if node.next:
                    node.next.prev = prev

                # in this case, prev doesn't move
                node = node.next
            else:
                prev = node
                node = node.next

        return dummy.next


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
        ([1, 2, 3, 1, 4], 1, [2, 3, 4]),
        ([2, 3, 1, 4, 2], 2, [3, 1, 4]),
        ([9, 9, 9], 9, [])
    ]

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        dll = list_to_doubly_linkedlist(arr)
        output = s.deleteAllOccurrences(dll, target)
        result = doubly_linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")


