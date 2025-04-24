from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    """
    Given the head of a doubly linked list with its values sorted 
    in non-decreasing order. Remove all duplicate occurrences of 
    any value in the list so that only distinct values are present 
    in the list. 

    Return the head of the modified linked list.
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in linked list
    def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = head, head.next

        while node:
            if node.val == prev.val:
                # remove it
                prev.next = node.next
                if node.next:
                    node.next.prev = prev

                # in this case, prev doesn't move
            else:
                prev = node

            node = node.next

        return head



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
        ([0, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([1, 1, 1, 2, 2], [1, 2]),
        ([9, 9, 9], [9])
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        dll = list_to_doubly_linkedlist(arr)
        output = s.removeDuplicates(dll)
        result = doubly_linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
