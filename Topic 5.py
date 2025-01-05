class Order:
    def __init__(self, order_id, item_name, quantity, priority):
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.priority = priority

    def __repr__(self):
        return f"Order(order_id={self.order_id}, item_name={self.item_name}, quantity={self.quantity}, priority={self.priority})"

class InventoryManagement:
    def __init__(self):
        self.orders = []  # Dynamic array (list) to track orders

    def add_order(self, order):
        # Add a new order to the list
        self.orders.append(order)

    def update_order(self, order_id, **kwargs):
        # Find and update an order based on order_id
        for order in self.orders:
            if order.order_id == order_id:
                order.item_name = kwargs.get('item_name', order.item_name)
                order.quantity = kwargs.get('quantity', order.quantity)
                order.priority = kwargs.get('priority', order.priority)
                break

    def remove_order(self, order_id):
        # Remove an order from the list based on order_id
        self.orders = [order for order in self.orders if order.order_id != order_id]

    def get_orders(self):
        # Return the list of orders
        return self.orders

# Example usage
if __name__ == "__main__":
    inventory_system = InventoryManagement()

    # Adding orders
    inventory_system.add_order(Order(1, "Apples", 100, 3))
    inventory_system.add_order(Order(2, "Bananas", 150, 2))
    inventory_system.add_order(Order(3, "Carrots", 200, 1))

    # Updating an order
    inventory_system.update_order(2, quantity=180, priority=4)

    # Removing an order
    inventory_system.remove_order(1)

    # Retrieving and displaying orders
    orders = inventory_system.get_orders()
    for order in orders:
        print(order)
