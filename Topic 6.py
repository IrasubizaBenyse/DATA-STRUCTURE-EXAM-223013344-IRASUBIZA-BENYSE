class TreeNode:
    def __init__(self, name, data=None):
        self.name = name  # Name of the node (e.g., category name)
        self.data = data  # Additional data (e.g., product information)
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        # Add a child node to the current node
        self.children.append(child_node)

    def remove_child(self, child_node):
        # Remove a child node from the current node
        self.children = [child for child in self.children if child != child_node]

    def get_child(self, name):
        # Find a child node by name
        for child in self.children:
            if child.name == name:
                return child
        return None

    def display(self, level=0):
        # Display the tree structure
        indent = " " * (level * 4)
        print(f"{indent}{self.name} ({self.data if self.data else 'Category'})")
        for child in self.children:
            child.display(level + 1)

# Example usage
if __name__ == "__main__":
    # Creating the root node (supermarket)
    root = TreeNode("Supermarket")

    # Creating category nodes
    fruits = TreeNode("Fruits")
    vegetables = TreeNode("Vegetables")
    dairy = TreeNode("Dairy")

    # Adding category nodes to the root
    root.add_child(fruits)
    root.add_child(vegetables)
    root.add_child(dairy)

    # Adding subcategory/product nodes
    fruits.add_child(TreeNode("Apples", {"stock": 100, "price": 1.2}))
    fruits.add_child(TreeNode("Bananas", {"stock": 150, "price": 0.8}))
    vegetables.add_child(TreeNode("Carrots", {"stock": 200, "price": 0.5}))
    dairy.add_child(TreeNode("Milk", {"stock": 50, "price": 1.0}))
    dairy.add_child(TreeNode("Cheese", {"stock": 30, "price": 3.5}))

    # Displaying the tree
    root.display()
