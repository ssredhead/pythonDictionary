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

  #Write a method which returns the node that is n nodes from the tail of the linked list.

  #If n is 0, we would return the tail node, if n is 1, we would return the second to last node, 
  # and so on.

  #takes one argument:
  #the number of nodes counting from the tail.
  #return the node instance at that location.
  def n_from_last(self, n):
    nodes_left = self.size() - 1 - n #size - 1 because ll stats at index 0, - n to get the node from tail to return
    tracker = 0
    current = self.head
    while tracker < nodes_left:
      current = current.next
      tracker += 1
  
    return current

  def remove_duplicates(self):
    prev = self.head #start with head
    current = prev.next #get second node in list
    while current.next is not None: #until the end of the list
      if prev.val == current.val: #if the values are the same (duplicates)
        current = current.next #this is the duplicate, move the current pointer to the next node
        prev.next = current #this is the original. Move it's pointer to the node after the duplicate
        #this essentially "removes" the duplicate
      else:
        #If they aren't duplicates, move prev 1 node right, move current 1 node right (no skips)
        prev.next = current
        current = current.next
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