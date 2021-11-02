# flatten() removes nested lists but keeps the values contained within
#break all the sublists down to elements
def flatten(my_list):
  result = []

  for el in my_list:
    #if element is a list, recursive case:
    if isinstance(el, list):
      print("list found!")
      #recurse with list element
      flat_list = flatten(el)
      result += flat_list
    else:
      #base case - el is not a list. append it to result list
      result.append(el)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))
