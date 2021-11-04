# Here’s how we’ll accomplish the implementation of heapsort:

# Build a max-heap to store the data from an unsorted list.
# Extract the largest value from the heap and place it into a sorted list.
# Replace the root of the heap with the last element in the list. Then, rebalance the heap.
# Once the max-heap is empty, return the sorted list.

# import heap class
from max_heap import MaxHeap 

# create a heapsort function
def heapsort(lst):
  # create an empty list
  sort = []

  # make an instance of MaxHeap
  max_heap = MaxHeap()

  # add values from lst to max_heap
  for el in lst:
    max_heap.add(el)

  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    #insert max_value to start of sort list
    sort.insert(0, max_value)
  return sort

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
# print the sorted list
print(sorted_list)

#output:
# Adding: 99 to [None]
# Heapifying up
# Heap Restored [None, 99]
# Adding: 22 to [None, 99]
# Heapifying up
# Heap Restored [None, 99, 22]
# Adding: 61 to [None, 99, 22]
# Heapifying up
# Heap Restored [None, 99, 22, 61]
# Adding: 10 to [None, 99, 22, 61]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10]
# Adding: 21 to [None, 99, 22, 61, 10]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21]
# Adding: 13 to [None, 99, 22, 61, 10, 21]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21, 13]
# Adding: 23 to [None, 99, 22, 61, 10, 21, 13]
# Heapifying up
# Heap Restored [None, 99, 22, 61, 10, 21, 13, 23]
# Removing: 99 from [None, 99, 22, 61, 10, 21, 13, 23]
# Last element moved to first: [None, 23, 22, 61, 10, 21, 13]
# Heapifying down!
# Right child 61 is larger than left child 22
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 61, 22, 23, 10, 21, 13]

# Removing: 61 from [None, 61, 22, 23, 10, 21, 13]
# Last element moved to first: [None, 13, 22, 23, 10, 21]
# Heapifying down!
# Right child 23 is larger than left child 22
# HEAP RESTORED! [None, 23, 22, 13, 10, 21]

# Removing: 23 from [None, 23, 22, 13, 10, 21]
# Last element moved to first: [None, 21, 22, 13, 10]
# Heapifying down!
# Left child 22 is larger than right child 13
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 22, 21, 13, 10]

# Removing: 22 from [None, 22, 21, 13, 10]
# Last element moved to first: [None, 10, 21, 13]
# Heapifying down!
# Left child 21 is larger than right child 13
# HEAP RESTORED! [None, 21, 10, 13]

# Removing: 21 from [None, 21, 10, 13]
# Last element moved to first: [None, 13, 10]
# Heapifying down!
# There is only a left child
# HEAP RESTORED! [None, 13, 10]

# Removing: 13 from [None, 13, 10]
# Last element moved to first: [None, 10]
# HEAP RESTORED! [None, 10]

# Removing: 10 from [None, 10]
# Last element moved to first: [None]
# HEAP RESTORED! [None]

# [10, 13, 21, 22, 23, 61, 99]