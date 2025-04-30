from typing import Optional

class ListNode:
    def __init__(self, x: int, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    A linked list of length n is given such that each node contains an
    additional random pointer, which could point to any node in the list,
    or null.  Return a deep copy of the linked list.

    LC. 138 Copy List with Random Pointer
    """

    # Analysis: time = O(n), space = O(n)
    # where n = number of nodes in linked list
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None

        old_to_new = {}

        # First pass, get nodes
        current = head
        while current:
            old_to_new[current] = ListNode(current.val)
            current = current.next
        
        # print([n.val for n in old_to_new])
        # Second pass, get their random connections
        current = head
        while current:
            clone = old_to_new[current]
            clone.next = old_to_new.get(current.next)
            clone.random = old_to_new.get(current.random)
            current = current.next
        
        return old_to_new[head]

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

def compare_lists(original, clone):
    visited = set()
    while original and clone:
        if original.val != clone.val:
            return False
        if (original.random and clone.random and original.random.val != clone.random.val) or \
           (original.random is None and clone.random is not None) or \
           (original.random is not None and clone.random is None):
            return False
        if id(original) == id(clone):
            return False  # not a deep copy
        if id(clone) in visited:
            return False  # cycle in clone
        visited.add(id(clone))
        original = original.next
        clone = clone.next
    return original is None and clone is None


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    a = ListNode(7)
    b = ListNode(13)
    c = ListNode(11)
    d = ListNode(10)
    e = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    b.random = a
    c.random = e
    d.random = c
    e.random = a

    clone = s.copyRandomList(a)
    assert compare_lists(a, clone)

    # Test case 2
    a = ListNode(1)
    b = ListNode(2)

    a.next = b
    a.random = a
    b.random = b

    clone = s.copyRandomList(a)
    assert compare_lists(a, clone)

    # Test case 3
    clone = s.copyRandomList(None)
    assert clone is None

    print("All test cases passed!")