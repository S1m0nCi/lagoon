class Stack():
  typeName = "stack"

  def __init__(self, bottom) -> None:
    self.stack = [bottom]

  def add(self, item) -> None:
    self.stack.append(item)

  def pop(self) -> None:
    self.stack.pop()

  def peek(self):
    return self.stack[len(self.stack) - 1]
  
  def __repr__(self):
    return str(self.stack)
  
my_stack = Stack('S')

my_name = "Simon"
for letter in my_name[1:]:
  my_stack.add(letter)

print (my_stack)

