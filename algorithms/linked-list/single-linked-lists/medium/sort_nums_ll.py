from typing import Optional

class ListNode:
    def __init__(self, num: int = 0, next = None):
        self.val = num
        self.next = next


class Solution:
    """
    Given the head of a singly linked list consisting of only 0, 1 or 2. 
    Sort the given linked list and return the head of the modified list. 
    Do it in-place by changing the links between the nodes without creating 
    new nodes.
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes
    def sortList(self, head:Optional[ListNode]):
        current = head
        zero_tail = one_tail = two_tail = None
        zero_head = one_head = two_head = None

        while current:
            next_node = current.next
            current.next = None # break the link to avoid cycles

            if current.val == 0:
                if not zero_tail:
                    zero_head = zero_tail = current
                else:
                    zero_tail.next = current
                    zero_tail = zero_tail.next

            elif current.val == 1:
                if not one_tail:
                    one_head = one_tail = current
                else:
                    one_tail.next = current
                    one_tail = one_tail.next

            else: # current.val == 2
                if not two_tail:
                    two_head = two_tail = current
                else:
                    two_tail.next = current
                    two_tail = two_tail.next

            current = next_node

        # Note that 'or' will choose the non-None option
        if zero_tail:
            zero_tail.next = one_head or two_head
        if one_tail:
            one_tail.next = two_head

        return zero_head or one_head or two_head


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
        ([2, 1, 0], [0, 1, 2]),
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2], [2, 2, 2]),
        ([0, 2, 1, 1, 0, 2], [0, 0, 1, 1, 2, 2]),
        ([1], [1]),
        ([0, 2], [0, 2]),
        ([2, 0], [0, 2])
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        head = list_to_linkedlist(inp)
        sorted_head = s.sortList(head)
        result = linkedlist_to_list(sorted_head)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
