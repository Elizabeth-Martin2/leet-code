class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    """Perform basic operations on a doubly linked list"""

    # Analysis: time = O(n), space = O(1)
    # where n = len(arr)
    def constructDLL(self, arr):
        """Constructs a doubly linked list from a gien integer array."""
        if not arr:
            return None
        
        node = Node(arr[0])
        head = node
        
        for i in range(1, len(arr)):
            current_node = Node(arr[i])
            node.next = current_node
            current_node.prev = node
            node = current_node
            
        return head


    # Analysis: time = O(p), space = O(1)
    def addNode(self, head, p, x):
        """
        Adds a node right after a given position (p) with a given value (x)
        in a doubly linked list
        """
        node = head

        for _ in range(p):
            node = node.next

        new_node = Node(x)

        new_node.prev = node
        new_node.next = node.next

        if node.next is not None:
            node.next.prev = new_node

        node.next = new_node

        return head


    # Analysis: time = O(x), space = O(1)
    def delete_node(self, head, x):
        """Deletes a node at a given position (x) in a doubly linked list"""
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head

        last_node = node = head

        for _ in range(0, x - 1):
            last_node = node
            node = node.next

        if node.next is None:
            last_node.next = None
        else:
            last_node.next = node.next
            node.next.prev = last_node

        return head


    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes
    def reverseDLL(self, head):
        """Reverses a doubly linked list"""
        if not head or not head.next:
            return head

        current = head

        while current:
            current.next, current.prev = current.prev, current.next
            head = current
            current = head.prev

        return head


if __name__ == "__main__":
    solution = Solution()

    def dll_to_list(head):
        res = []
        while head:
            res.append(head.data)
            head = head.next
        return res

    # Construction & addition test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 99, [1, 2, 3, 99, 4, 5]),
        ([10, 20, 30, 40], 0, 15, [10, 15, 20, 30, 40]),
        ([5, 15, 25, 35], 3, 45, [5, 15, 25, 35, 45])
    ]

    for i, (arr, pos, val, expected) in enumerate(test_cases, 1):
        head = solution.constructDLL(arr)
        head = solution.addNode(head, pos, val)
        output = dll_to_list(head)
        assert output == expected, f"Construction & Addition test {i} failed, expected {expected}, got {output}"

    # Deletion test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([10, 20, 30, 40], 1, [20, 30, 40]),
        ([5, 15, 25, 35], 4, [5, 15, 25])
    ]

    for i, (arr, pos, expected) in enumerate(test_cases, 1):
        head = solution.constructDLL(arr)
        head = solution.delete_node(head, pos)
        output = dll_to_list(head)
        assert output == expected, f"Deletion test {i} failed, expected {expected}, got {output}"

    # Reverse test cases
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([10, 20, 30, 40], [40, 30, 20, 10]),
        ([5, 15, 25, 35], [35, 25, 15, 5])
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        head = solution.constructDLL(arr)
        head = solution.reverseDLL(head)
        output = dll_to_list(head)
        assert output == expected, f"Reversing test {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")
