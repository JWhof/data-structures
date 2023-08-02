from node import Node

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def __repr__(self) -> str:
        "A visual representation of the nodes. NOTE: uses an array to keep track of all of the nodes, demonstration purposes only."
        current = self.head
        list_of_nodes = []

        if current == None:
            return "Linked list: None"

        while current != None:
            list_of_nodes.append(current)
            current = current.next

        return "Linked list: " + ' => '.join([node.data for node in list_of_nodes])

    def len(self) -> int:
        "Returns 0-indexed integer length of the linked list."
        count = -1
        current = self.head

        while current != None:
            current = current.next
            count += 1

        return count
    
    def look_up(self, index: int) -> None or Node:
        "Given an element index, returns corresponding node or None if index is invalid."
        current = self.head
        count = 0

        while current != None and count < index:
            current = current.next
            count += 1

        if current == None:
            return None
        
        return current

    def insert_node(self, node_to_add: Node, index: int)  -> None or Node:
        "Given an index and a node, returns node if successfully inserted or None if index is invalid."
        previous = None
        current = self.head
        count = 0

        if index == 0:
            previous = node_to_add
            previous.next = current
            self.head = previous
            

        while current != None and count < index:
            previous = current
            current = current.next
            count += 1
        
        if count > index:
            return None
        
        previous.next = node_to_add
        node_to_add.next = current
        return node_to_add
    

    def remove_node(self, node_to_remove: Node) -> None or Node:
        "Given a node, returns node if successfully removed or None if node is not in list."
        current = self.head
        previous = None
        count = 0
        len = self.len()

        if current == None:
            return None
        
        while current != node_to_remove and count < len:
            previous = current
            current = current.next
            count += 1

        if count >= len:
            return None

        previous.next = current.next
        current = None
        return node_to_remove
    
    def remove_index(self, index: int) -> None or Node:
        "Given an index, returns corresponding node if successfully remove or None if node is not in list."
        current = self.head
        previous = None
        count = 0

        if current == None:
            return None
        
        while current != None and count < index:
            previous = current
            current = current.next
            count += 1
        
        if count > index:
            return None
        
        previous.next = current.next
        return current

# Example usage

node_one = Node("First node")
my_linked_list = LinkedList(node_one)
print(my_linked_list.len()) # Should print 0
print(my_linked_list)

node_two = Node("Second node")
my_linked_list.insert_node(node_two, my_linked_list.len()+1)
print(my_linked_list.len()) # Should print 1
print(my_linked_list)

node_three = Node("Third node")
my_linked_list.insert_node(node_three, my_linked_list.len()+1)
print(my_linked_list.len()) # Should print 2
print(my_linked_list)

my_linked_list.remove_node(node_two)
print(my_linked_list.len()) # Should print 1
print(my_linked_list)

my_linked_list.insert_node(node_two, 0)
print(my_linked_list.len()) # Should print 2
print(my_linked_list)

node_four = Node("Fourth node")
my_linked_list.insert_node(node_four, 1)
print(my_linked_list.len()) # Should print 3
print(my_linked_list)

my_linked_list.remove_index(2)
print(my_linked_list.len()) # Should print 2
print(my_linked_list)