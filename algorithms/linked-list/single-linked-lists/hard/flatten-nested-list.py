from typing import Optional

class ListNode:
    def __init__(self, value:int = 0, child = None, next = None):
        self.val = value
        self.child = child
        self.next = next

# Helper functions for testing
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

class Solution:
    """
    Given a linked list of head nodes where each has a sorted child
    list connected via .child pointers, return a single linked list
    of sorted nodes.

    Example:
        Top-level (.next):   3 → 2 → 1 → 4 → 6 → 5
        Child pointers:      |    |    |         |
                             10   7    9         8
                                       |
                                       11
                                       |
                                       12

        Expected flattened output (sorted):
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12
    """

    # Merge function analysis:
    # time = O(n) , space = O(1)
    # where n = max(number of nodes in l1, number of nodes in l2)
    @staticmethod
    def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy head to hold new merged list
        merged_head = ListNode(0)
        merged = merged_head

        # Merge lists based on values
        while l1 and l2:
            if l1.val <= l2.val:
                merged.child = l1
                l1 = l1.child
            else:
                merged.child = l2
                l2 = l2.child

            merged = merged.child

        # Get remaining values if there are any
        merged.child = l1 if l1 else l2

        return merged_head.child

    # Flatten list function analysis:
    # time = O(n log m) , space = O(1)
    # where n = total number of nodes and m = number of linked lists
    def flattenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        merged = None

        while current:
            merged = Solution.merge(merged, current)  # O(n) / function call
            current = current.next

        # dummy head to hold new merged list
        current = merged
        while current:
            current.next = current.child
            current.child = None
            current = current.next

        return merged


if __name__ == "__main__":
    s = Solution()

    # Create top-level nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    # Connect horizontal (next)
    node3.next = node2
    node2.next = node1
    node1.next = node4
    node4.next = node6
    node6.next = node5

    # Create child lists
    node3.child = ListNode(10)
    node2.child = ListNode(7)
    node1.child = ListNode(9)
    node5.child = ListNode(8)

    node6.child = ListNode(11)
    node6.child.child = ListNode(12)

    # Flatten and test
    head = node3
    flattened = s.flattenList(head)
    output = linkedlist_to_list(flattened)

    print("Flattened output:", output)
    expected = [1,2,3,4,5,6,7,8,9,10,11,12]
    print("Expected:", expected)

    assert output == expected, "Test failed!"
    print("Test passed!")
