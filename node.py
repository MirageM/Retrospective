class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

def calculate_height(node):
   if node is None:
      return 0
   left_height = calculate_height(node.left)
   right_height = calculate_height(node.right)
   return max(left_height, right_height) + 1

print(calculate_height(root))