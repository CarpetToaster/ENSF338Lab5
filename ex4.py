import random
import timeit
import matplotlib.pyplot as plt

# Part 1

class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = item


    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return item

# Part 2

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def setData(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node



    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        item = self.head.getData()
        self.head = self.head.getNext()
        if self.head == None:
            self.tail = None
        return item

# Part 3
def randomTasks(tasks):
    taskList = []
    for i in range (tasks):
        probabilityValue = random.random()

        if probabilityValue <= 0.7:
            taskList.append("enqueue")

        else:
            taskList.append("dequeue")
    return taskList

# Part 4

def performTaskList(taskList, queueType):
    if queueType == "ArrayQueue":
        queue = ArrayQueue(len(taskList))
    else:
        queue = LinkedQueue()

    for task in taskList:
        if task == "enqueue":
            queue.enqueue(1)
        else:
            queue.dequeue()

# Part 4

tasks = 10000
trials = 100
timeitNumber = 5
taskList = randomTasks(tasks)

arrayTimes = []
linkedTimes = []

for i in range(trials):
    randomTasks(tasks)
    arrayTime = timeit.timeit("performTaskList(taskList, 'ArrayQueue')", globals = globals(), number = timeitNumber)
    linkedTime = timeit.timeit("performTaskList(taskList, 'LinkedQueue')", globals = globals(), number = timeitNumber)
    arrayTimes.append(arrayTime/ timeitNumber)
    linkedTimes.append(linkedTime/ timeitNumber)

print(f'The average time for the Array implementation was {sum(arrayTimes)/ timeitNumber}, the minimum time was {min(arrayTimes)}, the maximum time was {max(arrayTimes)}')
print(f'The average time for the Linked list implementation was {sum(linkedTimes)/ timeitNumber}, the minimum time was {min(linkedTimes)}, the maximum time was {max(linkedTimes)}')

# Part 5
x = range(len(arrayTimes))

plt.plot(x, arrayTimes, label="ArrayQueue Times", color='blue')
plt.plot(x, linkedTimes, label="LinkedQueue Times", color='red')
plt.xlabel("Trial Number")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison of ArrayQueue and LinkedQueue")
plt.legend()
plt.show()

# Part 5 discussion
# The graph shows the both implementations have linear time complexity, and are take similar amounts of time
# to execute. However, the linked lists implementation is slightly faster in this case.
# This could be due to the array implementation performing more checks/comparisons than the linked lists implementation
# as well as the array queue performing more calculations. Where the array version performs modulus operations,
# the linked lists version simply works with pointers.