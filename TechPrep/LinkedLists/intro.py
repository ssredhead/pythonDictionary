# Linked lists are a sequential data structure. 
# A linked list consists of nodes which store data and a link to another node. 
# Each node knows its location, what value it holds, and where to find the next node in the linked list. 
# The first node is the head node, and the last node is the tail node.

# Nodes of a linked list are stored anywhere in the computer’s memory unlike an array (or list), 
# where values are stored sequentially in memory. 
# The actual memory address is abstracted away from us by Python. 
# With our Node class, we use the instance property .next to represent the location 
# of the following node.

# Due to the difference in memory storage, linked lists are more efficient
#  than arrays at inserting and deleting values; arrays are more efficient at looking up values.

# In an array, inserting a value causes every subsequent value to be shifted over to make room. 
# In a linked list, inserting a value requires a change of .next for the preceding node.

# With an index, we can retrieve any value in a list in constant time. 
# Linked lists have no index because nodes are located all over the computer’s memory. 
# We must traverse, or move through each node starting at the head, to find a value. 
# The traversal takes linear time.



from linked_list import LinkedList, Node

# initializing linked list with NO head node to start
linked_list_1 = LinkedList()
linked_list_1.add('hey!')
linked_list_1.add('ho!')
linked_list_1.add("let's go!")
linked_list_1.traverse()
# The last added node is the head using .add()!

# We can also add nodes without .add()!
# assigning a Node's .next property directly...
lyric_node_1 = Node('cool')
lyric_node_2 = Node('beans!')
lyric_node_1.next = lyric_node_2

# initializing a linked list WITH a head node
linked_list_2 = LinkedList(lyric_node_1)
print(linked_list_2)

# We can also build up a linked list with a loop!
current_node = Node("Let's count to 5!")
# save a reference to the head to pass to LinkedList
head = current_node 
for i in range(1, 6):
  current_node.next = Node(i) 
  current_node = current_node.next

linked_list_3 = LinkedList(head) # passing head as argument
print(linked_list_3)
print("This linked list has {0} nodes!".format(linked_list_3.size()))


#Output:
# Starting traversal from head
# visiting node: let's go!
# visiting node: ho!
# visiting node: hey!
# Traversal complete
# cool -> beans! -> 
# Let's count to 5! -> 1 -> 2 -> 3 -> 4 -> 5 -> 
# This linked list has 6 nodes!