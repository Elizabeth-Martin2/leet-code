# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given a linked list, rearrange the nodes so that all the odd indexed nodes
    are first then followed by all the even indexed nodes.

    Note: you must complete this in O(n) time and O(1) extra space.

    LC. 328 Odd Even Linked List
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in linked list
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


# Helper functions for testing
def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def extract_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4], [1, 3, 2, 4]),
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ]

    for i, (input_list, expected_list) in enumerate(test_cases, 1):
        head = build_list(input_list)
        result = s.oddEvenList(head)
        output_list = extract_list(result)
        assert output_list == expected_list, f"Test case {i} failed: expected {expected_list}, got {output_list}"

    print("All test cases passed!")
