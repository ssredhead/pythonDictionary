# A linked list is a sequential chain of nodes. 

#Build a node class first
class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

# my_node = Node(44)

# print(my_node.get_value())


# Create your LinkedList class:
# It should be able to:
# get the head node of the list (like peeking at the first item in line)
#add a new mode to the beginning (head) of the list
#print the list values in order
#remove a node that has a particular value
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    #create new node (from Node class)
    new_node = Node(new_value)
    #use Node function set_next_node to point new node to original head node (making it the new head of the list)
    new_node.set_next_node(self.head_node)
    #reassign self.head_node as new_node
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if (current_node.get_value() == value_to_remove):
      #if the value to be removed is the head node, make the second node in the ll the new head by calling the get_next_node function.
      self.head_node = current_node.get_next_node()
    else:
        #check in case the list has ended
      while current_node:
      #look at the value 1 node ahead to see if it is the value to remove. If not, iterate.
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
            #essentially, skip over the node with value_to_remove
          current_node.set_next_node(next_node.get_next_node())
          #set the removed node value to none to truly remove it
          current_node = None
        else:
            #iterate, value_to_remove not found
          current_node = next_node

ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
