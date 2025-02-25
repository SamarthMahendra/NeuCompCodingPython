class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        newnode = Node(value)
        if self.size == 0:
            self.head = self.tail = newnode
            self.head.next = self.head.prev = self.head
        else:
            newnode.prev = self.tail
            newnode.next = self.head
            self.head.prev = newnode
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return True
        if self.size == 0:
            return False
        else:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1  # Head is the front

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1  # Tail is the rear

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()