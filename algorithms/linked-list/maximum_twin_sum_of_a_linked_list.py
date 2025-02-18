# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Attempt 1: O(n)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twin_vals = []
        current = head
        max_val = i = n = 0
        
        while current: # O(n)
            twin_vals.append(current.val)
            current = current.next
        
        n = len(twin_vals)
        while i <= n/2: # O(n/2) = O(n)
            twin_node = n - 1 - i
            max_val = max(twin_vals[i] + twin_vals[twin_node], max_val)
            i += 1

        return max_val