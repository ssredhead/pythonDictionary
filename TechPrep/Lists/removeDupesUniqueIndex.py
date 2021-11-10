# remove duplicates 
# constant space
# return index of last unique element

# Clarifying Questions:

# Does the ordering of the duplicate(s) matter?
# No! They can be in any order.

# An in-place solution can optimize space complexity to O(1) (constant)
#To do this, sort the input list with all duplicates moved to the end, then remove them.
#The return value will be the index of the final unique value
#input: ['a', 'a', 'g', 't', 't', 'x', 'x', 'x']
#sorted: ['a', 'g', 't', 'x' 'a', 'x', 't', 'x']
#return index: 3, the index of the last unique value: 'x'

#dupe_list is a sorted list which may have duplicate values

#move all duplicates to the end of the list and maintain sorted order. 
#return: index of the last unique value

def move_duplicates(dupe_list):
  unique_idx = 0 #keep track of last unique index
  for i in range(len(dupe_list) - 1): # - 1 to compare next index
    if dupe_list[i] != dupe_list[i + 1]: #if value is unique, swap it's place with the current unique value.
      dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
      #increment unique_idx
      unique_idx += 1

  #swap value at last unique index with the last value in the list
  print("unique_idx", dupe_list[unique_idx])
  print("last_idx", dupe_list[len(dupe_list) - 1])
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  print("unique_idx after", dupe_list[unique_idx])
  print("last_idx after", dupe_list[len(dupe_list) - 1])
  return unique_idx

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']), 3, move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']) == 3))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']), 4, move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates([13, 13, 13, 13, 13, 42]), 1, move_duplicates([13, 13, 13, 13, 13, 42]) == 1))