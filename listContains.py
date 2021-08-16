#Check if a list contains item, and then if it contains item more than n times
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
