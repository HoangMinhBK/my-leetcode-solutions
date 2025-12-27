class LRUCache
=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @capacity = capacity
        @cache = Hash.new
        # Insert 2 dummy nodes in head and tail
        @head = Node.new(0,0) # dummy head
        @tail = Node.new(0,0) # dummy tail
        @head.next = @tail
        @tail.prev = @head
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        if @cache.has_key?(key)
            remove_node(@cache[key])
            insert_node_at_end(@cache[key])
            return @cache[key].value
        else
            return -1
        end
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        node = Node.new(key, value)
        if @cache.has_key?(key)
            remove_node(@cache[key])
        end
        @cache[key] = node
        insert_node_at_end(node)
        
        if @cache.length > @capacity
            actual_head = @head.next
            remove_node(actual_head)
            @cache.delete(actual_head.key)
        end
    end

    def remove_node(node)
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
    end

    # Insert new node after the actual node and before the dummy node
    # Ex: (1,1) <-> (2,2) <-> (0,0)
    #     insert (3,3)
    #     (1,1) <-> (2,2) <-> (3,3) <-> (0,0)
    def insert_node_at_end(node)
        dummy_tail = @tail
        actual_tail = @tail.prev

        actual_tail.next = node
        node.prev = actual_tail
        node.next = dummy_tail
        dummy_tail.prev = node
    end

end

class Node
    attr_accessor :key, :value, :next, :prev
    def initialize(key, value)
        @key=key
        @value=value
        @next=nil
        @prev=nil
    end
end
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)