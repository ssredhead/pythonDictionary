from node import Node
# Create the Queue class:
#Queues are FIFO
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

    #enqueue, add to tail
  def enqueue(self, value):
    #check if bounded queue has space
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      #check if queue is empty
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
        self.size += 1
    else:
      #bounded queue is out of space
      print("Sorry, no more room!")

  def dequeue(self):
    if not self.is_empty():
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.size == 1:
        self.head = None
        self.tail = None
      else:
        #nodes are removed from the head
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
    
  def peek(self):
    if self.size > 0:
        #get value from Node class function
      return self.head.get_value()
    else:
      print("Nothing to see here!")
  
  # Define get_size() and has_space() if the queue is bounded:
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
