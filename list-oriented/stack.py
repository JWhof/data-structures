from node import Node

class Stack:
    def __init__(self, head=None) -> None:
        self.head = head

    def __repr__(self) -> str:
        "Returns a visual representation of the stack. NOTE: uses arrays, for demonstration purposes only."
        stack = []
        current = self.head
        while current != None:
            stack.append(current)
            current = current.next
        return "\n".join([str(node) for node in stack])
    
    def push(self, node: Node) -> Node:
        "Pushes a node to the top of the stack."
        node.next = self.head
        self.head = node
        return node
    
    def pop(self) -> None or Node:
        "Removes the top node from the stack."
        node_to_remove = None
        if self.head != None:
            node_to_remove = self.head
            self.head = node_to_remove.next
        return node_to_remove


node_one = Node("First node")
my_stack = Stack(node_one)

node_two = Node("Second node")
my_stack.push(node_two)

print(my_stack)
print(format("-", "->10"))

node_three = Node("Third node")
my_stack.push(node_three)
print(my_stack)
print(format("-", "->10"))

my_stack.pop()
print(my_stack)
