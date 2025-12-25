class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)  # dummy head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        dummy_tail = self.tail  # Node (0,0)
        actual_tail = dummy_tail.prev

        actual_tail.next = node
        node.prev = actual_tail
        node.next = dummy_tail
        dummy_tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = None
        self.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
