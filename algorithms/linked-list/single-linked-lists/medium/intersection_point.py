from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Given the heads of two lists, return the intersection node if it exists, otherwise
    return None.

    LC. 160 Intersection of Two Linked Lists
    """

    # Optimized Analysis: time = O(n + m), space = O(1)
    # where n = length of list A and m = length of list B
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        nodeA, nodeB = headA, headB
        lenA, lenB = 1, 1 
        
        # Get length of lists & check the ends for early exit
        while nodeA.next:
            lenA += 1
            nodeA = nodeA.next
        
        while nodeB.next:
            lenB += 1
            nodeB = nodeB.next

        if nodeA != nodeB:
            return None
        
        # We know there's an intersection, chop heads until same length
        nodeA, nodeB = headA, headB
        while lenA > lenB:
            nodeA = nodeA.next
            lenA -= 1
        
        while lenB > lenA:
            nodeB = nodeB.next
            lenB -= 1

        # March forward until we find intersection
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return nodeA

    # Brute force analysis: time = O(n + m) space = O(n)
    # where n = length of list A and m = length of list B
    def getIntersectionNodeBF(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seenA = []

        nodeA, nodeB = headA, headB

        while nodeA:
            seenA.append(nodeA)
            nodeA = nodeA.next

        while nodeB:
            if nodeB in seenA:
                return nodeB
            
            nodeB = nodeB.next
        
        return None



# Helper functions for testing
def build_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def attach_tail(head, tail):
    if not head:
        return tail
    current = head
    while current.next:
        current = current.next
    current.next = tail
    return head


if __name__ == "__main__":
    s = Solution()

    # Test 1: Intersecting lists
    intersect = build_linked_list([8, 10])
    headA = attach_tail(build_linked_list([3, 7]), intersect)
    headB = attach_tail(build_linked_list([99, 1]), intersect)
    assert s.getIntersectionNode(headA, headB) == intersect, "Test 1 failed"

    # Test 2: No intersection
    headA = build_linked_list([1, 2, 3])
    headB = build_linked_list([4, 5, 6])
    assert s.getIntersectionNode(headA, headB) is None, "Test 2 failed"

    # Test 3: Intersection at head
    shared = build_linked_list([1, 2, 3])
    headA = shared
    headB = shared
    assert s.getIntersectionNode(headA, headB) == shared, "Test 3 failed"

    # Test 4: One list is empty
    headA = None
    headB = build_linked_list([1, 2, 3])
    assert s.getIntersectionNode(headA, headB) is None, "Test 4 failed"

    # Test 5: Both lists are empty
    headA = None
    headB = None
    assert s.getIntersectionNode(headA, headB) is None, "Test 5 failed"

    print("All test cases passed!")

