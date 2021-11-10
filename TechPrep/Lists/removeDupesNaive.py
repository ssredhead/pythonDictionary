# remove duplicates 
# no time/space requirements
# return a list with duplicates removed

# Clarifying Questions:

# Are there constraints on time or space efficiency?
# No! Any solution will do.
# Is it okay to alter the input list?
# You can alter the list or return a new list.

def remove_duplicates(dupe_list):
  unique_list = []

  for value in dupe_list:
    if value not in unique_list:
      unique_list.append(value)
  return unique_list

#O(N) time complexity (linear) since you go through all elements
#O(N) space complexity, because you create a new list

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']), ['a', 'x', 'g', 't'], remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a', 'x', 'g', 't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']), ['c', 'd', 'e', 'f', 'a'], remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == ['c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [13, 42], remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))