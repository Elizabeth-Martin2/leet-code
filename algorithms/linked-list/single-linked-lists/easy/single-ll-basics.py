from typing import Optional
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    """Perform basic operations on a singly linked list"""

    # Analysis: time = O(n), space = O(1)
    # where n = len(arr)
    def constructLL(self, arr):
        """Build a linked list from a given integer array"""
        if not arr:
            return None
        
        node = Node(arr[0])
        head = node
        
        for i in range(1, len(arr)):
            node.next = Node(arr[i])
            node = node.next
        
        return head


    # Anaysis: time = O(n), space = O(1)
    # where n = len(arr)
    def insertAtEnd(self,head,x):
        """Insert an integer at the end of a linked list"""
        if not head:
            return Node(x)

        node = head
        while node.next is not None:
            node = node.next

        node.next = Node(x)
        return head


    # Analysis: time = O(1), space = O(1)
    def deleteNode(self, node):
        """
        Delete a node from a linked list when
        only given the node to be deleted
        """
        node.data = node.next.data
        node.next = node.next.next


    # Analysis: time = O(n), space = O(1)
    # where n = number of nodes
    def getCount(self, head):
        """Return the number of nodes in a linked list"""
        node = head
        count = 0

        while node:
            count += 1
            node = node.next

        return count


    # Analysis: time = O(n), space = O(1)
    def searchKey(self, n, head, key):
        """
        Search a linked list for a key and return true or false
        if present.
        """
        node = head

        while node:
            if node.data == key:
                return True
            node = node.next

        return False


    # Analysis: time = O(n), space = O(1)
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


if __name__ == "__main__":

    # Used for test cases
    def linkedListToList(head):
        result = []
        while head:
            result.append(head.data)
            head = head.next
        return result

    sol = Solution()

    # constructLL tests
    constructLL_tests = [
        ([], []),
        ([5], [5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ]

    for i, (arr, expected) in enumerate(constructLL_tests, 1):
        head = sol.constructLL(arr)
        assert linkedListToList(head) == expected, f"constructLL Test {i} failed"

    # insertAtEnd tests
    insertAtEnd_tests = [
        ([1, 2, 3], 4, [1, 2, 3, 4]),
        ([], 10, [10])
    ]

    for i, (arr, x, expected) in enumerate(insertAtEnd_tests, 1):
        head = sol.constructLL(arr)
        head = sol.insertAtEnd(head, x)
        assert linkedListToList(head) == expected, f"insertAtEnd Test {i} failed"

    # deleteNode tests
    head = sol.constructLL([1, 2, 3, 4, 5])
    node_to_delete = head.next.next
    sol.deleteNode(node_to_delete)
    assert linkedListToList(head) == [1, 2, 4, 5], "deleteNode Test failed"

    # getCount tests
    getCount_tests = [
        ([1, 2, 3, 4, 5], 5),
        ([], 0),
        ([7], 1)
    ]

    for i, (arr, expected) in enumerate(getCount_tests, 1):
        head = sol.constructLL(arr)
        assert sol.getCount(head) == expected, f"getCount Test {i} failed"

    # searchKey tests
    searchKey_tests = [
        ([10, 20, 30, 40, 50], 30, True),
        ([10, 20, 30, 40, 50], 100, False),
        ([], 5, False)
    ]

    for i, (arr, key, expected) in enumerate(searchKey_tests, 1):
        head = sol.constructLL(arr)
        assert sol.searchKey(len(arr), head, key) == expected, f"searchKey Test {i} failed"

    print("All test cases passed!")








