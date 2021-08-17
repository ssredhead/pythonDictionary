def double_index(lst, index):
  #check if index is too high
  if index > len(lst):
    return lst
  else:
    #Get lst up to index
    new = lst[:index]
  #double value of index
  new.append(lst[index]*2)
  #add the rest of the list
  new = new + lst[index+1:] 

  return new

print(double_index([3, 8, -10, 12], 2))
