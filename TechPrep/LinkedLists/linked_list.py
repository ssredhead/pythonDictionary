from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  #Write a method for .insert() that takes two values
  #the value which will be used to initialize a Node
  #the insertion location for the node instance
  #return self at the end of the function
  def insert(self, node_value, location):
    if not location: #if no location or location is 0, it will be the head node
      self.add(node_value) #use the .add method to make it the head
      return self
    
    prev = self.head #set up prev and current pointers to reorganize insertion
    current = prev.next
    new_node = Node(node_value)

    while location > 1: #decrement location is it goes through the linked list. Stop at 1 because of the decrement, it would overlap wit the head assigning
      prev = current #while decrement, move the prev and current pointers along
      current = current.next
      location -= 1
    
    #Once at the correct location, point prev toward new_node, and new_node to current.
    prev.next = new_node
    new_node.next = current

    return self

  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head
    
  def traverse(self):
    head = self.head
    print("Starting traversal from head")
    while head:
      print("visiting node: {0}".format(head.val))
      head = head.next
    print("Traversal complete")
    
  def size(self):
    node_count = 0
    current_node = self.head
    while current_node:
      node_count += 1
      current_node = current_node.next
    return node_count
  
  def __repr__(self):
    text = ''
    head = self.head
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text