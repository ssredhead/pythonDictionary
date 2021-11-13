from linked_list import LinkedList, Node, set_up_test_case

linked_list_1, linked_list_2 = set_up_test_case()
print(linked_list_1)
print(linked_list_2)

# Nodes within a linked list can be referenced multiple times. 
# We’ll explore this idea with a partially merged linked list.

# a -> b
#        \
#         -> c -> e
#        /
# d -> f

# In this example, two different heads (nodes holding 'a' and 'd') merge 
# into a single linked list with the node holding 'c'. 
# This “merge point” results from nodes holding 'b' and 'f' both referencing 
# the node holding 'c' as the .next property.

# Write a function that returns the merge point node of two linked lists if it exists.

# # x -> a -> b
#            \
#             -> q -> e
#            /
#      d -> f
# return: node holding 'q'
 
# r
#  \
#   -> x
#  /
# f
# return: node holding 'x'
 
# j -> k
# l -> q
# return: None

# return the first node referenced by both linked lists, 
# or None if such a node does not exist.

def merge_point(linked_list_a, linked_list_b):
  #optimal solution is to remove the difference in size between (for loop)
  # the two linked lists and then traverse both simultaneously (while loop)
  size_a = linked_list_a.size()
  size_b = linked_list_b.size()

  traverse = abs(size_a - size_b) 
  print(traverse)

  #determine which ll is larger and set their head variables accordingly
  if size_a > size_b:
    bigger = linked_list_a.head
    smaller = linked_list_b.head
  else:
    bigger = linked_list_b.head
    smaller = linked_list_a.head

  #now use bigger ll to traverse over difference of sizes 
  # (get head kickstarted for longer ll until they are even and congruent nodes 
  # can be compared side by side)
  for i in range(traverse):
    bigger = bigger.next
    #the two nodes that represent both lists have an equal number of steps 
    # until the tail node (so check for ending of one list).
    while bigger and smaller:
      print(bigger.val)
      print(smaller.val)
    #complete the traversal and check for matching nodes along the way
      if bigger == smaller:
        #if they match, the join is found, return it
        return bigger
      #if not, iterate still in the while loop
      bigger = bigger.next
      smaller = smaller.next
  #if the for/while loop ends, a join was not found, so return None
  return None

#This approach takes O(N) -linear time since the while loop compares the indexes only once

test_result = merge_point(linked_list_1, linked_list_2)

print("Function should return merge point node holding 'q': {0}".format(test_result.val))