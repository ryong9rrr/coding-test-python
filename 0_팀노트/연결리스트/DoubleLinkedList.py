class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    def desc(self, reverse = False):
        nodes = []
        if reverse == False:
            node = self.head
            while node:
                nodes.append(node.data)
                node = node.next
        else:
            node = self.tail
            while node:
                nodes.append(node.data)
                node = node.prev
        return nodes
    
    def add(self, new_node):
        if not isinstance(new_node, Node):
            return
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def remove(self, target_node):
        if not isinstance(target_node, Node):
            return
        if self.head == target_node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == target_node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev_node = target_node.prev
            next_node = target_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
    
    def insert(self, target_node):
        if not isinstance(target_node, Node):
            return
        if target_node.prev is None:
            self.head.prev = target_node
            self.head = target_node
        elif target_node.next is None:
            self.tail.next = target_node
            self.tail = target_node
        else:
            node = target_node.prev
            node.next.prev = target_node
            node.next = target_node