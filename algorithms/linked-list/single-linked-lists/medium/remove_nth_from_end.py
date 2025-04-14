from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given a linked list (head) and an integer n, return the list after removing the
    nth node from the end of the list.

    LC. 19 Remove Nth node from end of list
    """

    # Single pass analysis: time = O(m), space = O(1)
    # where m = number of nodes in list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


    # Double pass analysis: time = O(m), space = O(1)
    # where m = number of nodes in list
    def removeNthFromEndBF(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        count = 0

        # count length of LL
        while slow:
            slow = slow.next
            count += 1

        target = count - n
        if target == 0:
            return head.next

        count = 0
        prev = current = head

        while count < target:
            prev = current
            current = current.next
            count += 1

        if not current:
            prev.next = None
        else:
            prev.next = current.next

        return head


# helper functions for testing
def build_linked_list(nums: list[int]) -> Optional[ListNode]:
    head = ListNode(nums[0])
    current = head

    for num in range(1, len(nums)):
        current.next = ListNode(nums[num])
        current = current.next

    return head


def extract_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 2, [2])
    ]

    for i, (my_list, n, expected) in enumerate(test_cases, 1):
        temp = build_linked_list(my_list)
        output = solution.removeNthFromEnd(temp, n)
        output = extract_list(output)

        assert expected == output, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")




