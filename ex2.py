# ex2.py
import bisect
import random
import time

class PriorityQueue1:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        self.items = self.merge_sort(self.items)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

class PriorityQueue2:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        bisect.insort(self.items, item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None

def generate_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 1000)))
        else:
            tasks.append(('dequeue', None))
    return tasks

def run_tasks(tasks, pq_class):
    pq = pq_class()
    for op, val in tasks:
        if op == 'enqueue':
            pq.enqueue(val)
        else:
            pq.dequeue()

def measure_performance():
    times_pq1 = []
    times_pq2 = []
    for _ in range(100):
        tasks = generate_tasks()
        # Measure PriorityQueue1
        start = time.time()
        run_tasks(tasks, PriorityQueue1)
        times_pq1.append(time.time() - start)
        # Measure PriorityQueue2
        start = time.time()
        run_tasks(tasks, PriorityQueue2)
        times_pq2.append(time.time() - start)
    # Calculate averages
    avg_pq1 = sum(times_pq1) / len(times_pq1)
    avg_pq2 = sum(times_pq2) / len(times_pq2)
    print(f"Average time for PriorityQueue1: {avg_pq1:.6f} seconds")
    print(f"Average time for PriorityQueue2: {avg_pq2:.6f} seconds")

if __name__ == "__main__":
    measure_performance()

# Discussion of results:
# The PriorityQueue2 implementation is faster than PriorityQueue1 because inserting elements
# in the correct position using bisect.insort (O(n) per enqueue) is more efficient than
# appending and then performing a full O(n log n) merge sort after each enqueue. The repeated
# sorting in PriorityQueue1 leads to higher computational overhead, especially with frequent
# enqueue operations. PriorityQueue2 maintains the sorted order incrementally, which reduces
# the overall time complexity for enqueue-heavy tasks.