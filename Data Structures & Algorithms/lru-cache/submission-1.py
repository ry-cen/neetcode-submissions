class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prevNode = self.tail.prev
        self.tail.prev = node
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            rNode = self.head.next
            self.remove(rNode)
            del self.cache[rNode.key]
