from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in the list
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Count nodes in list
        tail, count = head, 1
        while tail.next:  # O(n)
            count += 1
            tail = tail.next

        k %= count
        # Early exit for no rotations required
        if k == 0:
            return head

        # Step 2: Walk to new head
        # print(f"There are {count} nodes in the list")
        prev, node = None, head
        steps_to_new_head = count - k
        
        for _ in range(steps_to_new_head):
            prev = node
            node = node.next
        
        # print(f"prev: {prev.val}, node: {node.val}")

        # Step 3: chop of remaining list & rotate
        prev.next = None
        tail.next = head

        return node


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
        ([1,2,3,4,5], 2, [4,5,1,2,3]),
        ([1,2,3,4,5], 10, [1,2,3,4,5]),
        ([1, 2], 5, [2, 1]),
        ([1, 2], 0, [1, 2])
    ]

    for i, (arr, k, expected) in enumerate(test_cases, 1):
        l1 = list_to_linkedlist(arr)
        output = s.rotateRight(l1, k)
        result = linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")
