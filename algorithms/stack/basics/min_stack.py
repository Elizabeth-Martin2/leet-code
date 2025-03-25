class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.arr:
            return -1
        else:
            temp = self.arr.pop()
            if temp == self.min_stack[-1]:
                self.min_stack.pop()
            return temp

    def top(self) -> int:
        if not self.arr:
            return -1
        else:
            return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else float('inf')



if __name__ == "__main__":
    s = MinStack()

    inputs = [5, 3, 7, 3, 2]
    for val in inputs:
        s.push(val)

    # Pop once (should remove 2, the current min)
    assert s.pop() == 2
    assert s.getMin() == 3

    # Pop again (should remove 3, the current min again)
    assert s.pop() == 3
    assert s.getMin() == 3

    # Push new min
    s.push(1)
    assert s.getMin() == 1

    # Top should return 1
    assert s.top() == 1

    # Pop 1, min should return to 3
    assert s.pop() == 1
    assert s.getMin() == 3

    # Clean up
    while s.pop() != -1:
        pass
    assert s.getMin() == float('inf')

    print("All test cases passed!")