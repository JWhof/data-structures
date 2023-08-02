from node import Node

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def __repr__(self) -> str:
        "Returns a string representation of the queue. NOTE: uses arrays. For demonstration purposes only."
        queue = []
        current = self.front

        while current != self.back:
            queue.append(current)
            current = current.next

        queue.append(self.back)
        
        return ' -> '.join([str(node) for node in queue])

    def enqueue(self, node) -> Node:
        "Adds a node to the back of the queue."
        if self.front == None:
            self.front = node
            self.back = node
        else:
            node_to_add = node
            self.back.next = node_to_add
            self.back = node_to_add
        return node
        
    
    def dequeue(self) -> None or Node:
        "Removes a node from the front of the queue."
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next

node_one = Node("First node")
my_queue = Queue()

my_queue.enqueue(node_one)

print(my_queue)

node_two = Node("Second node")
my_queue.enqueue(node_two)

print(my_queue)

node_three = Node("Third node")
my_queue.enqueue(node_three)

print(my_queue)

my_queue.dequeue()

print(my_queue)

my_queue.dequeue()

print(my_queue)
