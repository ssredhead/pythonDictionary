from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
    #normal tracker to go through the linked list node by node
  tail_seeker = linked_list.head_node
  #special tracker to stay n spaces away from tail_tracker that will land on the nth_to_last node
  nth_to_last = None
  count = 1

  #iterate through linked list normally. Increment count
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1

    #when count becomes n + 1 (because tail_seeker will not stop at the last node, but the "None" node afterward)
    #then start/iterate nth_to_last, maintaining the distance between tail_seeker and nth_to_last
    if count >= n + 1:
      if nth_to_last is None:
          #if this is the first time, set nth_to_last as head
        nth_to_last = linked_list.head_node
      else:
        nth_to_last = nth_to_last.get_next_node()
  return nth_to_last

def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)