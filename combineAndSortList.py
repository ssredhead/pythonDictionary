#This function combines two lists and then sorts them and returns the results
def combine_sort(lst1, lst2):
  first = lst1 + lst2
  sort = sorted(first)
  return sort


#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
