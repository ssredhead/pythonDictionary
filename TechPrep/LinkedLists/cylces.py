from linked_list import LinkedList, Node, build_cycle_linked_list, build_linked_list_no_cycle


cycle_linked_list = build_cycle_linked_list()
no_cycle_linked_list = build_linked_list_no_cycle()

# As we saw with the merge point problem, more than one node can reference another node. 
# These references can create a cycle in the linked list where the traversal will loop back on itself.

#Ex: 
#    -> b -> c
#  /      \   \
# a         d <-
 
# 'd' node's next points to 'b' node


# Write a function that detects whether a cycle exists in a linked list. 
# A cycle exists if traversing the linked list visits the same node more than once.

# A cycle does not mean repeated values. 
# Avoid this pitfall in your implementation by comparing the Node instances themselves, 
# not their values! (i.e. don't make a dictionary to simply store values and check for repeats)
# Ex:
# a = Node('a')
# other_a = Node('a')
 
# a.val == other_a.val 
#   True
# a == other_a
#   False
def has_cycle(linked_list):
    #use two pointers, slow, which moves once per loop, and fast, which moves twice
  slow = linked_list.head
  fast = linked_list.head
  while slow and fast:
    slow = slow.next #move slow ahead
    fast = fast.next #move fast ahead for the first time

    if fast: #If the end of the ll hasn't been reached, move fast
      fast = fast.next
    else: #If it has, there wasn't a cycle, and we can return false
      return False
    
    if slow == fast: #compare the nodes, not the values. If slow and fast are on the same node, fast has cycled back, return true
      return True

#This approach takes linear time (O(N)) and is an in-place solution, so O(1) space complexity

cycle_result = has_cycle(cycle_linked_list)
no_cycle_result = has_cycle(no_cycle_linked_list)

print("Should return True when a cycle exists: {0}".format(cycle_result))

print("Should return False when a cycle does not exist: {0}".format(no_cycle_result))

