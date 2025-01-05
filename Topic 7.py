class Order:
    def __init__(self, order_id, item_name, quantity, priority):
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.priority = priority

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, item_name={self.item_name}, "
                f"quantity={self.quantity}, priority={self.priority})")

def quick_sort_orders(orders):
    if len(orders) <= 1:
        return orders

    pivot = orders[len(orders) // 2].priority
    left = [order for order in orders if order.priority < pivot]
    middle = [order for order in orders if order.priority == pivot]
    right = [order for order in orders if order.priority > pivot]

    return quick_sort_orders(left) + middle + quick_sort_orders(right)

# Example usage
if __name__ == "__main__":
    orders = [
        Order(1, "Apples", 100, 5),
        Order(2, "Bananas", 150, 2),
        Order(3, "Carrots", 200, 8),
        Order(4, "Dates", 50, 1),
        Order(5, "Eggplants", 80, 3),
        Order(6, "Figs", 90, 10),
        Order(7, "Grapes", 120, 7),
    ]

    print("Before sorting:")
    for order in orders:
        print(order)

    sorted_orders = quick_sort_orders(orders)

    print("\nAfter sorting by priority:")
    for order in sorted_orders:
        print(order)
