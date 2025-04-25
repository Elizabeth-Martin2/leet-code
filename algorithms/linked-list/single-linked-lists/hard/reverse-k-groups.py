from typing import Optional

class ListNode:
    def __init__(self, val:int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a linked list, reverse the nodes of the list
    k at a time, and return the modified list.  k is a positive integer
    and is less than or equal to the length of the linked list. If the
    number of nodes is not a multiple of k then left-out nodes, in the
    end, should remain as it is.

    LC. 25 Reverse Nodes in k-Group
    """

    # Helper function to reverse segments of list
    # Note: start is inclusive, end is exclusive
    def reverse_segment(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        prev = end
        while start != end:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        return prev
  
    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes in linked list
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # first find length of the list
        dummy = ListNode(0, head)
        counter = 0
        node = dummy.next

        while node:
            counter += 1
            node = node.next

        # determine how many loops we have to do (to avoid leave-out nodes)
        rev_groups = counter // k

        # loop to go through that reversal groups
        prev, node = dummy, dummy.next
        for i in range(rev_groups):
            # get start and end nodes for reversing segment
            start = node
            for _ in range(k - 1):
                node = node.next

            node = node.next                    
            rev_head = self.reverse_segment(start, node)

            # connect end of reversed segment to start of the next
            prev.next = rev_head
            # setup for next loop
            prev = start

        return dummy.next


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
        ([1,2,3,4,5,6,7], 2, [2,1,4,3,6,5,7]),
        ([1,2,3,4,5,6], 2, [2,1,4,3,6,5]),
        ([1,2,3,4,5,6,7], 3, [3,2,1,6,5,4,7])
    ]

    for i, (nums, k, expected) in enumerate(test_cases, 1):
        linked_list = list_to_linkedlist(nums)
        output = s.reverseKGroup(linked_list, k)
        result = linkedlist_to_list(output)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"

    print("All test cases passed!")