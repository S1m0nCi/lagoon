class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def traverse():
    pass

class Tree():
  def __init__(self, root):
    self.root = Node(root)

  def preorder(self, start, records=[]):
    if start is not None:
      records.append(start.value)
      records = self.preorder(start.left, records)
      records = self.preorder(start.right, records)
      # we are reassigning records, as preorder adds to it, and we are using the new records each time.
    return records
  
  def postorder(self, start, records=[]):
    if start is not None:
      records = self.postorder(start.left, records)
      records = self.postorder(start.right, records)
      records.append(start.value)
    return records

bin_tree = Tree(5)
bin_tree.root.left = Node(3) 
bin_tree.root.right = Node(4)

print (bin_tree.preorder(bin_tree.root))
print (bin_tree.postorder(bin_tree.root))