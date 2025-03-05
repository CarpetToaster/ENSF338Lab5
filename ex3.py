import random
import timeit
import matplotlib.pyplot as plt
# Part 1
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()


# Part 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setData(self, value):
        self.value = value

    def setNext(self, next):
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.setNext(self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            return None
        else:
            popValue = self.head.getData()
            self.head =self.head.getNext()
            return popValue


# Part 3
def randomTasks(tasks):
    taskList = []
    for i in range (tasks):
        probabilityValue = random.random()

        if probabilityValue <= 0.7:
            taskList.append("push")

        else:
            taskList.append("pop")
    return taskList


# part 4
def performTaskList(taskList, stackType):
    if stackType == "ArrayStack":
        stack = ArrayStack()
    else:
        stack = LinkedStack()

    for task in taskList:
        if task == "push":
            stack.push(1)
        else:
            stack.pop()

    return None



arrayTimes = []
linkedTimes = []

trials = 100
tasks = 10000
taskList = randomTasks(tasks)

for i in range(trials):
    randomTasks(tasks)
    arrayTime = timeit.timeit("performTaskList(taskList, 'ArrayStack')", globals = globals(), number = 25)
    linkedTime = timeit.timeit("performTaskList(taskList, 'LinkedStack')", globals = globals(), number = 25)
    arrayTimes.append(arrayTime)
    linkedTimes.append(linkedTime)

print(arrayTimes)
print(linkedTimes)

# Part 5
x = range(len(arrayTimes))

plt.plot(x, arrayTimes, label="ArrayStack Times", color='blue')
plt.plot(x, linkedTimes, label="LinkedStack Times", color='red')
plt.xlabel("Trial Number")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison of ArrayStack and LinkedStack")
plt.legend()
plt.show()

# Part 5 discussion
# The results show that while both of these implementations have constant time complexity, The array
# implementation is faster than the linked list implementation.
# The reason for this is for each push in linked list a new object is created with the value, and then the
# head is updated. While for arrays it uses an optimized built in method.
# And for each pop operation, the linked list has to do a check, store the value, and then update the pointers.
# While again the array version has an optimized built in method for it.
