class MinStack
    attr_accessor :main_stack, :mono_stack
    def initialize()
        @main_stack = []
        @mono_stack = []
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push(val)
        main_stack.push(val)
        if mono_stack.empty? || mono_stack.last >= val
            mono_stack.push(val)
        end
    end


=begin
    :rtype: Void
=end
    def pop()
        val = main_stack.pop
        mono_stack.pop if val == mono_stack.last
    end


=begin
    :rtype: Integer
=end
    def top()
        main_stack.last
    end


=begin
    :rtype: Integer
=end
    def get_min()
        mono_stack.last
    end


end

# Your MinStack object will be instantiated and called as such:
# obj = MinStack.new()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()