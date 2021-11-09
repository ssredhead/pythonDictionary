# “rotate” a list, or move elements forward in a list by a number of spaces, k.
# Elements at the greatest index will “wrap around” to the beginning of the list.

# Clarifying Questions:
#   Are there constraints on time or space efficiency?
#       Nope! Just solve the problem.
#   Should I account for negative inputs?
#       The rotation input will always be positive.
#   What if the rotation is greater than the list length?
#       Continue wrapping!
# The “rotated” list would be the same as the original when k is equal to the length.

# rotate list
# no time/space requirements
# return "rotated" version of input list

#pop and insert approach
def rotate(my_list, num_rotations):
  count = num_rotations
  #rotate clockwise taking n values from the back of the list and appended in order onto the front
  for i in range(len(my_list)):
    while count > 0:
      #remove last value from list
      new_front = my_list.pop()
      #insert value to front of the list
      my_list.insert(0, new_front)
      #decrement count
      count -= 1
  return my_list

#index and slice manipulation
#We can also think of how the list will look at the end the number of rotations. 
# All elements up to but not including the rotation point index will be placed
#  at the end of all elements from the index to the end of the list.

# The slice operator, [], and a negative rotation input as the index
# will split the original list into two sub-lists which can be added together.
#when num_rotations = 3
#my_list[:-num_rotations]
# ['a', 'b']
#my_list[-num_rotations:]
# ['c', 'd' ,'e']
def rotate_2(my_list, num_rotations):
    my_list = my_list[-num_rotations:] + my_list[:-num_rotations]
    return my_list



#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))