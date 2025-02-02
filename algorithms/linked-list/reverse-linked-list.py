# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Attempt 2: O(n) where n = number of nodes
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, previous = head, None

        while current:
            temp = current.next
            current.next = previous 
            previous = current
            current = temp
        
        return previous


# Attempt 1: Brute force (not optimized)
# Analysis: O(2n) == O(n)
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is not None:
#             ll_stack = deque()
#             current_node = head
            
#             while current_node is not None:
#                 ll_stack.append(current_node.val)
#                 current_node = current_node.next

#             new_list = ListNode(val = ll_stack.pop(), next = None)
            
#             current_node = new_list
#             while ll_stack:
#                 current_node.next = ListNode(val = ll_stack.pop(), next = None)
#                 current_node = current_node.next
#             return new_list