class Solution:
    # Attempt 2 (Accepted)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        prev = None
        slow = fast = head

        # Note, fast is the pointer to the next node, not the value
        # that's why we can check if "fast" is None and not fast.next.next
        while fast and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return head


    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow