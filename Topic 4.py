import heapq

class Order:
    def __init__(self, order_id, priority):
        self.order_id = order_id
        self.priority = priority

    def __lt__(self, other):
        # Orders are compared based on their priority
        return self.priority < other.priority

class OrderHeap:
    def __init__(self, max_size):
        self.heap = []
        self.max_size = max_size

    def add_order(self, order):
        if len(self.heap) < self.max_size:
            heapq.heappush(self.heap, order)
        else:
            # If the heap is full, replace the lowest priority order if the new order has a higher priority
            if order.priority > self.heap[0].priority:
                heapq.heappushpop(self.heap, order)

    def get_orders(self):
        return sorted(self.heap, key=lambda order: order.priority, reverse=True)

# Example usage
if __name__ == "__main__":
    max_orders = 5
    order_heap = OrderHeap(max_orders)

    orders = [
        Order(1, 5),
        Order(2, 2),
        Order(3, 8),
        Order(4, 1),
        Order(5, 3),
        Order(6, 10),
        Order(7, 7),
    ]

    for order in orders:
        order_heap.add_order(order)

    # Retrieve and display orders sorted by priority
    sorted_orders = order_heap.get_orders()
    for order in sorted_orders:
        print(f"Order ID: {order.order_id}, Priority: {order.priority}")
