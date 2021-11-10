# find rotation point (ascending start)
# No time/space requirements
# return index of "rotation point" element

# Clarifying Questions:
# Are there constraints on time or space efficiency?
#   No! Any solution will do.
# Does the rotation direction matter?
#   This won’t affect the return value.
# What if the input isn’t rotated?
#   Return 0.
# Will the input only be one data type (string or int)?
#   No, it should work for characters or numbers

#given a sorted list -> all values will be ascending except where the rotation starts
def rotation_point(rotated_list):
  min_val = rotated_list[0] #default min is first index. If it hasn't been rotated, return 0
  
  for i in range(len(rotated_list) - 1): # subtract 1 from length so that i + 1 is the last index and does not go out of bounds
    if min_val > rotated_list[i + 1]: #compare min to next index. min should not be > than the next
      return i + 1 #if the next index is less than min, it is the rotation point. return the index
  return 0 #if the for loop ends, the list is in ascending order, the 0 index is the min

#Time complexity: O(n) because it runs through all values
#Space complexity: O(1) because there are no additional data structures

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))