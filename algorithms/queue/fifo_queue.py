from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()
        
    def enqueue(self, item:int) -> None:
        self.items.append(item)
    
    def dequeue(self) -> int:
        if len(self.items) == 0:
            return -1
        
        return self.items.popleft()
    
    def peek(self) -> None:
        if len(self.items) == 0:
            print("-1")
        
        print(self.items[0])


if __name__ == "__main__":
    numq = input()
    numq = int(numq)
    my_stack = Stack()

    for i in range(numq):
        query = input()
        query = query.split()

        if query[0] == "1":
            my_stack.enqueue(query[1])
        elif query[0] == "2":
            my_stack.dequeue()
        else:
            my_stack.peek()