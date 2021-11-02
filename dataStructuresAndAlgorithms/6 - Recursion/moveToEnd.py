# define move_to_end()
def move_to_end(lst, val):
  result = []
  #base case
  if len(lst) == 0:
    return []
  
  #if the first element is the value to be moved
  if lst[0] == val:
      #make result a copy of the list without the first element
    result += move_to_end(lst[1:], val)
    #then append the first element onto the end
    result.append(lst[0])
  else:
      #append the first element first, it isn't the one we want to move
    result.append(lst[0]) 
    #make result a copy of the rest of the list without the first element
    result += move_to_end(lst[1:], val)
  return result


# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))