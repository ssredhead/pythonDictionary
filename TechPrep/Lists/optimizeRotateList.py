# rotate list
# Constant space requirement
# return input list "rotated"

#optimizing the solution means reducing the memory required (space complexity)
#or reducing the number of instructions the computer must execute (time complexity)

#sometimes this means entirely rethinking the approach to a question.

#In the previous question the slice operator allowed an O(N) time and space complexity
#because the new list is made of copies of each value and every value is visited.

#The goal is to do better than O(N).
#Space complexity - create an in place soltuin without additonal data structures

# Given a list and a positive integer, return the same list “rotated” a number of times 
# that match the input integer. This time, we’ll rotate the list backward and use O(1) space.

def rotate(my_list, num_rotations):
  rotate_char = ""
  while num_rotations > 0:
    rotate_char = my_list.pop(0)
    my_list.append(rotate_char)
    num_rotations -= 1
  
  return my_list




#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['b', 'c', 'd', 'e', 'f', 'a'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['b', 'c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['c', 'd', 'e', 'f', 'a', 'b']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['e', 'f', 'a', 'b', 'c', 'd']))