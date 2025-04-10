from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a linked list check if the values of
    the nodes make a palindrome.

    LC.234 Palindrome Linked List
    """

    # Analysis: time = O(n), space = O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle
        current = nex = slow
        prev = None
        
        while current:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        
        # prev is now head of reversed half
        current = prev
        start = head

        while current:
            if current.val != start.val:
                return False
            
            current = current.next
            start = start.next

        return True


    # Brute force analysis: time = O(n), space = O(n)
    def isPalindromeBF(self, head: Optional[ListNode]) -> bool:
        temp = [str(head.val)]
        node = head
        
        while node and node.next:
            node = node.next
            if node:
                temp.append(str(node.val))
        
        temp = ''.join(temp)
        
        return temp == temp[::-1]


if __name__ == "__main__":

    def build_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        node = head
        for val in values[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

    test_cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
        ([1, 2], False),
        ([1], True),
        ([], True),
    ]

    sol = Solution()
    for i, (vals, expected) in enumerate(test_cases):
        head = build_linked_list(vals)
        result = sol.isPalindrome(head)
        print(f"Test case {i+1}: {vals} -> {result} (expected {expected}) {'✅' if result == expected else '❌'}")
