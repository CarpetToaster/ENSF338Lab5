# ex5.py

# Part 1: Array-based Circular Queue
class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Points to the front element
        self.rear = -1   # Points to the rear element
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.queue[self.front]
        print(f"peek {item}")
        return item

# Part 2: Circular Linked List-based Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front
        else:
            self.rear.next = new_node
            new_node.next = self.front
            self.rear = new_node
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.front.data
        if self.size == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.front.data
        print(f"peek {item}")
        return item

# Part 3: Test Case with 40 operations
def test_queue(queue):
    # Operations:
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.peek()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.peek()
    queue.enqueue(6)
    queue.enqueue(7)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    queue.dequeue()
    queue.peek()
    queue.dequeue()
    queue.enqueue(10)
    queue.enqueue(11)
    queue.dequeue()
    queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    queue.enqueue(15)
    queue.dequeue()
    queue.dequeue()
    queue.peek()

if __name__ == "__main__":
    print("Testing Array-based Queue:")
    q_array = CircularQueueArray(3)
    test_queue(q_array)

    print("\nTesting Linked List-based Queue:")
    q_ll = CircularQueueLinkedList(3)
    test_queue(q_ll)