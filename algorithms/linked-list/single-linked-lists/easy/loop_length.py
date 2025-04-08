class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    """
    Given the head of a linked list, return the number of
    nodes in a loop in the list.  If there are no loops,
    return 0.
    """

    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes
    def countNodesInLoop(self, head: Node):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # loop detected
                current = slow.next
                count = 1
                while current != slow:
                    current = current.next
                    count += 1
                return count

        return 0


if __name__ == "__main__":
    s = Solution()

    # Test Case 1: No loop
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    assert s.countNodesInLoop(head1) == 0

    # Test Case 2: Full loop (1 -> 2 -> 3 -> 1)
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    head2.next.next.next = head2
    assert s.countNodesInLoop(head2) == 3

    # Test Case 3: Partial loop (3 -> 4 -> 5 -> 3)
    head3 = Node(1)
    head3.next = Node(2)
    head3.next.next = Node(3)
    head3.next.next.next = Node(4)
    head3.next.next.next.next = Node(5)
    head3.next.next.next.next.next = head3.next.next  # 5 -> 3
    assert s.countNodesInLoop(head3) == 3

    # Test Case 4: Single node, no loop
    head4 = Node(10)
    assert s.countNodesInLoop(head4) == 0

    # Test Case 5: Single node with loop to itself
    head5 = Node(99)
    head5.next = head5
    assert s.countNodesInLoop(head5) == 1

    print("All test cases passed!")
