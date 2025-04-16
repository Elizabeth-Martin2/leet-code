from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given a linked list, return a new list with the nodes sorted.

    LC. 148 Sort List
    """

    # Merge function analysis: time = O(n), space = O(1)
    # where n = number of nodes in left + right
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(0)
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            
            tail = tail.next
        
        tail.next = left or right
        return dummy.next

    # SortList function analysis (including helper function)
    # time = O(n log n) , space = O(log n) (from recursion stack)
    # where n = number of nodes in linked list
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # split linked list in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)

        return self.merge(left, right)


    # Brute force analysis: time = O(n log n), space = O(n)
    # where n = number of nodes
    def sortListBF(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        temp = []

        current = head
        while current:
            temp.append(current.val)
            current = current.next
        
        temp.sort()
        current = ListNode(temp[0])
        new_head = current
        for i in range(1, len(temp)):
            current.next = ListNode(temp[i])
            current = current.next
        
        return new_head