def eval_rpn(tokens)
  operators = Set.new(["+", "-", "*", "/"])
  stack = []

  tokens.each do |token|
    if operators.include?(token)
        b = stack.pop.to_i
        a = stack.pop.to_f
        # Do the calculation and then push the result back to stack.
        # Ex: a.send("/",b) means a/b in Ruby
        stack.push(a.send(token, b).to_i)
    else
        stack.push(token)
    end
  end

  stack.last.to_i
end