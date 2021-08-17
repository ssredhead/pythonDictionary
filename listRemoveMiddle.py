#based on start and end indexes, remove all indexes between them. Return result
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:] #everything up to start index (not inclusive) + everything past end index + 1 to exclude end


#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
