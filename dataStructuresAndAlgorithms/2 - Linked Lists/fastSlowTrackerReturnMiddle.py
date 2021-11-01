from LinkedList import LinkedList

def find_middle(linked_list):
  fast_tracker = linked_list.head_node
  slow_tracker = linked_list.head_node

    #iterate fast_tracker normally
  while fast_tracker:
    fast_tracker = fast_tracker.get_next_node()
    if fast_tracker:
        #iterate fast tracker twice for every one slow_tracker
        # to get the middle node by the time fast_tracker reaches the end
      fast_tracker = fast_tracker.get_next_node()
      slow_tracker = slow_tracker.get_next_node()

  return slow_tracker

  #an alternative method
#   def find_middle_alt(linked_list):
    #   count = 0
    #   fast = linked_list.head_node
    #   slow = linked_list.head_node
    #   while fast:
    #     fast = fast.get_next_node()
    #     if count % 2 != 0:
    #       slow = slow.get_next_node()
    #     count += 1
#       return slow
  

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)