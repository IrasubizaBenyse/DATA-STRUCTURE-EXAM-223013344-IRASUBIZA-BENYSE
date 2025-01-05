# Binary Tree Node Class
def binary_tree_node(data):
    return {'data': data, 'left': None, 'right': None}

# Insert Function for Binary Tree
def insert(root, data):
    if root is None:
        return binary_tree_node(data)
    if data < root['data']:
        root['left'] = insert(root['left'], data)
    else:
        root['right'] = insert(root['right'], data)
    return root

# In-Order Traversal for Binary Tree
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root['left'])
        print(root['data'], end=' ')
        inorder_traversal(root['right'])

# Circular Queue Class
class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        index = self.front
        while index != self.rear:
            print(self.queue[index], end=' ')
            index = (index + 1) % self.max_size
        print(self.queue[index])

# Example usage:
# Binary Tree
root = None
elements = [50, 30, 20, 40, 70, 60, 80]
for el in elements:
    root = insert(root, el)

print("In-Order Traversal of the Binary Tree:")
inorder_traversal(root)
print()

# Circular Queue
cq = CircularQueue(5)
print("Enqueue operations:")
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

print("Dequeue operations:")
cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue(60)
cq.enqueue(70)
cq.display()
