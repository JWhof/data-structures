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
            return

        if node.left == None or node.right == None: # Single child internal node case
            child = node.left
            
            if child == None:
                child = node.right

            child.parent = node.parent
            
            if child.parent == None:
                child = self.root
            elif node.value < node.parent.value:
                node.parent.left = child
            else:
                node.parent.right = child
            return
        
        #TODO: add internal node with two children case


        
        



    def find_value(self, current: TreeNode, value: int) -> None or TreeNode:
        "Finds a given value using recursion."
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
            if value > current.value:
                current = current.right
        return current

my_binary_search_tree = BinarySearchTree()

node_one = TreeNode(1)

my_binary_search_tree.insert_tree_node(node_one)

node_two = TreeNode(2)

print(my_binary_search_tree.find_value(my_binary_search_tree.root, 1))
print(my_binary_search_tree.find_value_iterative(my_binary_search_tree.root, 1))
