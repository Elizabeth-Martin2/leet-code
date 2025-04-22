from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given a linked list where each node represents a digit in a number,
    return the linked list after adding 1 to the number.

    E.g., given 1 -> 2 -> 3 -> 4  , return 1 -> 2 -> 3 -> 5
    E.g., given 1 -> 2 -> 3 -> 9  , return 1 -> 2 -> 4 -> 0
    """

    # Helper function to reverse the linked list
    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in the list
    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in the list
    def addOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_head = self.revList(head)

        carry = 1
        current = rev_head

        prev = None
        while carry and current:
            current.val += carry
            carry = current.val // 10
            current.val = current.val % 10

            prev = current
            current = current.next

        if carry:
            prev.next = ListNode(1)

        return self.revList(rev_head)



# helper functions
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2, 1, 0], [2, 1, 1]),
        ([3, 6, 9], [3, 7, 0]),
        ([1, 0, 0], [1, 0, 1]),
        ([9, 9, 9], [1, 0, 0, 0])
    ]

    for i, (number_list, expected) in enumerate(test_cases, 1):
        head = list_to_linkedlist(number_list)
        output = s.addOne(head)
        result = linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")