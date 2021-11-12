# max sub sum
# no time/space requirements
# return maximum contiguous sum in list
# A sub-list is an uninterrupted portion of the list (up to and including the entire list)

# Clarifying Questions:

# Are there constraints on time or space efficiency?
# No! Any solution will do.
# Are all the numbers positive?
# No! Negative numbers can be in the input.
# How big or small can the sub-list be?
# From a single element to the entire list.

# input: [1, -7, 2, 15, -11, 2]

def maximum_sub_sum(my_list):
  max_sum = my_list[0] #1

  for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)): #gets index next to i
      if max_sum < sum(my_list[i:j + 1]): #1 < my_list[0] + my_list[1] (because range is not inclusive)
        max_sum = sum(my_list[i:j + 1]) #reassign if the sum is higher
        #run inner loop until indexes are exhausted, then go to outer loop to move right 1 index and start process again
  
  return max_sum

#Time complexity: O(n^3) because you loop through the list n * n * n times with the two for loops and the sum (copied list)
#Space complexity: O(n) because we copy my_list with the slice operator




#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, 2, 3, 4, 5]), 15, maximum_sub_sum([1, 2, 3, 4, 5]) == 15))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]), -1, maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]) == -1))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, -7, 2, 15, -11, 2]), 17, maximum_sub_sum([1, -7, 2, 15, -11, 2]) == 17))