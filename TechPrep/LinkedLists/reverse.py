from linked_list import LinkedList, Node

test_linked_list = LinkedList()

test_linked_list.add('d')
test_linked_list.add('c')
test_linked_list.add('b')
test_linked_list.add('a')

# a -> b -> c -> d
# d -> c -> b -> a
# We reassign each node’s .next property to the preceding node. 
# For the head node, this means .next points to None.

def reverse(linked_list):
  prev = None
  current = linked_list.head

  while current is not None: #until the end of the list
    temp = current.next #temporarily get the next node, since it's pointer will be lost
    current.next = prev #reverse the pointer to the previous node
    prev = current #move prev to current space
    current = temp #move current to original next node

  return LinkedList(prev) #return linked list version of prev

#This is an inorder solution (O(1) space complexity) that runs in linear time O(N)


print("Pre-reverse: {0}".format(test_linked_list))

reversed_linked_list = reverse(test_linked_list)

print("Post-reverse: {0}".format(reversed_linked_list))