
####### TEST INPUTS HERE
small = [1, 0, 1]
medium = [4, 2, 1, 3, 0, 1, 2] #water only rises to the second highest wall
#a submerged bar will "displace" water
edge_case = [0, 1, 0] #collects no water

####### NAIVE SOLUTION HERE
#find the maximums based on the "walls" to the left and right. Walls = greatest values
def rain_water(histogram): #python list of positive ints
  total_water = 0
  #start by finding the maximum value at a lesser index for each value in the list
  #ignore first and last index
  for i in range(1, len(histogram) - 1): #O(n^2) because of loop and slice operator
    left_values = histogram[:i] #assign left_values to everything up to but not including the current index
    left_max = max(left_values)
    print("Left max is: {0}".format(left_max))
    right_values = histogram[i:]
    right_max = max(right_values)
    print("Right max is: {0}".format(right_max))
    #it only fills to the second highest wall.
    if left_max < right_max:
      fill_mark = left_max
    else:
      fill_mark = right_max
    #subtract current value from fill_mark to account for displaced water
    displaced = fill_mark - histogram[i]
    if displaced > 0:
      #but only if the operation is value is positive
      total_water += displaced
  print("Total water is: {0}".format(total_water))
  return total_water

####### OPTIMIZED SOLUTION HERE
#store max value and compare to each index
def optimized_rain_water(histogram):
  max_value = histogram[0]
  total = 0
  #we need to know the relative max at each index
  left_maxes = []
  right_maxes = []
  for i in range(len(histogram)):
    print(f"Left max is {histogram[i]}")
    if histogram[i] > max_value:
      max_value = histogram[i]
    #list tracking the max value seen at each index moving from the left to the right
    left_maxes.append(max_value)
  
  max_value = histogram[-1] #now right maxes
  for j in range(len(histogram) - 1, -1, -1):
    #last index to first index, reverse for loop
    print(f"Right max is {histogram[j]}")
    if histogram[j] > max_value:
      max_value = histogram[j]
    right_maxes.append(max_value)
  right_maxes.reverse() #reverse it to match direction of left_maxes
  for k in range(len(histogram)):
    #take the min (shorter wall) of the two maxes at the current index, subtact the current histogram value (displaced water) and add it to the total water.
     total += min(left_maxes[k], right_maxes[k]) - histogram[k]
  print(total)
  return total
