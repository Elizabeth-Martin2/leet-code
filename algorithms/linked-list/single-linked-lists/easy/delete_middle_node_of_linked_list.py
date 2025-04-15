from typing import Optional

class ListNode:
    def __init__(self, val:int = 0, next = None):
        self.next = next
        self.val = val

class Solution:
    """
    Given a linked list, remove the middle node.

    LC. 2095 Delete the Middle Node of a Linked List
    """

    # Analysis: time = O(n), space = O(1)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        fast = slow = prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head


# --- Helpers ---
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

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([1], []),
        ([1, 2], [1]),
        ([1, 2, 3], [1, 3]),
        ([10, 20, 30, 40, 50, 60], [10, 20, 30, 50, 60])
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        head = build_list(input_list)
        result = s.deleteMiddle(head)
        output = extract_list(result)
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")
