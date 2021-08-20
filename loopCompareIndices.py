#If the values at the indices match, add the index to a new list and return it.
def same_values(lst1, lst2):
  i_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      i_lst.append(index)
  return i_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
