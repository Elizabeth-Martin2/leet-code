from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given two linked lists representing numbers in reversed order,
    return a new linked list with their sum.

    LC. 2 Add Two Numbers
    """

    # Analysis: time = O(n), space = O(n)
    # where n = max(number of nodes in l1, number of nodes in l2)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node1, node2 = l1, l2
        res_head = ListNode(0)
        res_node = res_head
        
        while node1 or node2:
            node1_val = node1.val if node1 else 0
            node2_val = node2.val if node2 else 0

            node_sum = node1_val + node2_val + carry
            
            res_val = node_sum % 10
            carry = node_sum // 10
            res_node.next = ListNode(res_val)
            res_node = res_node.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        if carry:
            res_node.next = ListNode(carry)
            res_node = res_node.next
        
        return res_head.next



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
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2,4,3], [5,6,4], [7,0,8]),
        ([9,9], [1], [0,0,1]),
        ([9,9,9], [1], [0,0,0,1]),
        (None, [2], [2])
    ]

    for i, (num1, num2, expected) in enumerate(test_cases, 1):
        l1 = list_to_linkedlist(num2)
        l2 = list_to_linkedlist(num1)
        output = s.addTwoNumbers(l1, l2)
        result = linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")

