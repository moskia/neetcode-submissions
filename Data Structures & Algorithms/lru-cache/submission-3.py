class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node: Node):
        """Unlink node from wherever it sits in the list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node):
        """Insert node right after head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        node = self.cache.get(key)
        self._remove(node)
        self._add_to_front(node)
        return node.value

    
    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        if key in self.cache:
            self._remove(self.cache.get(key))

        self.cache[key] = node
        self._add_to_front(node)

        if self.capacity < len(self.cache):
            extra_node = self.tail.prev
            self._remove(extra_node)
            self.cache.pop(extra_node.key)