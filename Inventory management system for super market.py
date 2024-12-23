# Topic 1: Define Data Structures and Their Importance
"""
Data structures play a vital role in inventory management systems for supermarkets. 
They organize data efficiently, ensuring quick retrieval and manipulation for tasks such as stock tracking, 
order processing, and category management. Efficient use of data structures minimizes errors and enhances performance.

Key Data Structures:
1. Arrays: Static inventory lists for predictable data.
2. Queues: Managing order processing (e.g., customer orders).
3. Linked Lists: Dynamic data insertion/deletion.
4. Trees: Representing hierarchical product categories.
5. Heaps: Prioritizing urgent tasks or orders.
6. Sorting Algorithms (e.g., Quick Sort): Optimizing inventory searches and organization.
"""

# Topic 2: Implement Binary Tree and Circular Queue

# Binary Tree Implementation
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = TreeNode(key, value)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = TreeNode(key, value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Circular Queue Implementation
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full!")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item

# Topic 3: Implement Doubly Linked List

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

# Topic 4: Create Heap for Order Management

import heapq

class OrderHeap:
    def __init__(self):
        self.heap = []

    def add_order(self, priority, order):
        heapq.heappush(self.heap, (priority, order))

    def process_order(self):
        if not self.heap:
            print("No orders to process!")
            return None
        return heapq.heappop(self.heap)[1]

# Topic 5: Use Array for Dynamic Data Tracking

class InventoryArray:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

# Topic 6: Implement Tree for Hierarchical Data

class CategoryNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Topic 7: Use Quick Sort

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example Usage (Optional)
if __name__ == "__main__":
    # Binary Tree Example
    inventory_tree = BinaryTree()
    inventory_tree.insert(101, "Apples")
    inventory_tree.insert(205, "Bananas")
    inventory_tree.insert(150, "Carrots")
    print(inventory_tree.search(205))  # Output: Bananas

    # Circular Queue Example
    orders_queue = CircularQueue(5)
    orders_queue.enqueue("Order 1")
    orders_queue.enqueue("Order 2")
    print(orders_queue.dequeue())  # Output: Order 1

    # Doubly Linked List Example
    dll = DoublyLinkedList()
    dll.append(101, "Apples")
    dll.append(205, "Bananas")
    dll.delete(101)

    # Order Heap Example
    order_heap = OrderHeap()
    order_heap.add_order(1, "Order A")
    order_heap.add_order(3, "Order C")
    order_heap.add_order(2, "Order B")
    print(order_heap.process_order())  # Output: Order A

    # Array Example
    inventory = InventoryArray()
    inventory.add_item("Milk")
    inventory.add_item("Bread")
    inventory.remove_item("Milk")

    # Tree Example
    root = CategoryNode("Food")
    fruits = CategoryNode("Fruits")
    vegetables = CategoryNode("Vegetables")
    root.add_child(fruits)
    root.add_child(vegetables)

    # Quick Sort Example
    inventory_data = [45, 12, 78, 23]
    sorted_data = quick_sort(inventory_data)
    print(sorted_data)  # Output: [12, 23, 45, 78]



