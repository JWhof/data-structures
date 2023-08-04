from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root
    
    def insert_tree_node(self, node: TreeNode):
        "Inserts a node into the tree."
        if self.root == None:
            self.root = node
            return
        self.insert_node(self.root, node)
    
    def insert_node(self, current: TreeNode, node: TreeNode):
        "Used for recursion. NOTE: to insert a node into the tree, please use insert_tree_node."
        if node.value == current.value: # If the nodes are the same, do nothing. Can be changed. 
            return
        if node.value < current.value:
            if current.left == None:
                current.left = node
                node.parent = current
            else:
                current = current.left
                self.insert_node(current, node) # Recursion until leaf node is found
        else:
            if current.right == None:
                current.right = node
                node.parent = current
            else:
                current = current.right
                self.insert_node(current, node)
    

    def remove_node(self, node) -> None or TreeNode:
        "Removes a node from the tree. NOTE: to pass in a value to remove, use the self.find_node(value) function as a parameter."
        # Cases: removing a leaf node, removing an internal node with one child, and removing an internal node with two children
        if self.root == None or node == None: # Check that tree is not empty
            return None
        
        if node.left == None and node.right == None: # Leaf node case
            if node == self.root:
                self.root = None
            elif node.value < node.parent.value:
                node.parent.left = None
            else:
                node.parent.right = None
            return node

        if node.left == None or node.right == None: # Single child internal node case
            child = node.left

            if child == None:
                child = node.right

            child.parent = node.parent
            
            if child.parent == None:
                self.root = child
            elif node.value < node.parent.value:
                node.parent.left = child
            else:
                node.parent.right = child
            return node
        
        successor = node.right # Two children internal node case
        while successor.left != None:
            successor = successor.left
        self.remove_node(successor)

        if node.parent == None:
            self.root = successor 
        elif node.parent.left == node:
            node.parent.left = successor
        else:
            node.parent.right = successor
        
        successor.parent = node.parent
        successor.left = node.left
        
        successor.right = node.right
        if node.right != None:
            node.right.parent = successor
        
        return node

    def find_value(self, current: TreeNode, value: int) -> None or TreeNode:
        "Finds a given value using recursion. NOTE: pass in self.root for the current parameter (first)."
        if current == None:
            return None
        if value < current.value and current.left != None:
            return self.find_value(current.left, value)
        if value > current.value and current.right != None:
            return self.find_value(current.right, value)
        if value == current.value:
            return current
        return None

    def find_value_iterative(self, current: TreeNode, value: int) -> None or TreeNode:
        "Finds a given value using iteration."
        while current != None and value != current.value:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        return current

my_binary_search_tree = BinarySearchTree()

node_one = TreeNode(3)

my_binary_search_tree.insert_tree_node(node_one)

node_two = TreeNode(7)
my_binary_search_tree.insert_tree_node(node_two)


print(my_binary_search_tree.find_value(my_binary_search_tree.root, 3))
print(my_binary_search_tree.find_value_iterative(my_binary_search_tree.root, 3))

node_three = TreeNode(4)
my_binary_search_tree.insert_tree_node(node_three)

node_four = TreeNode(11)
my_binary_search_tree.insert_tree_node(node_four)

print(f"Node with value 7 left child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 7).left.value}") # Should print 4
print(f"Node with value 7 right child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 7).right.value}") # Should print 11

# The binary tree looks like this:
#               3
#                \
#                 7
#                / \
#               4  11
# We now try to remove node 7:

my_binary_search_tree.remove_node(my_binary_search_tree.find_value(my_binary_search_tree.root, 7))

print(f"Node with value 11 left child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 11).left.value}") # Should print 4
print(f"Node with value 11 right child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 11).right}") # Should print None


# The binary tree now looks like this:
#               3
#                \
#                11
#                /
#               4
# We now try to remove node 11:

my_binary_search_tree.remove_node(my_binary_search_tree.find_value(my_binary_search_tree.root, 11))
print(f"Node with value 4 left child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 4).left}") # Should print None
print(f"Node with value 4 right child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 4).right}") # Should print None

# The binary tree now looks like this:
#               3
#                \
#                 4
# We now try to remove node 3:

my_binary_search_tree.remove_node(my_binary_search_tree.find_value(my_binary_search_tree.root, 3))
print(f"Node with value 4 left child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 4).left}") # Should print None
print(f"Node with value 4 right child: {my_binary_search_tree.find_value(my_binary_search_tree.root, 4).right}") # Should print None

# The binary tree now looks like this:
#               4
# We now try to remove node 4:

my_binary_search_tree.remove_node(my_binary_search_tree.find_value(my_binary_search_tree.root, 4))
print(f"Binary tree root value: {my_binary_search_tree.root}")

# And we're done! :)