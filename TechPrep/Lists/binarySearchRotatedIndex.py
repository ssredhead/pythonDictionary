# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

#target value will be less than both the next and previous values 

#use a modified binary search to reduce time complexity
#input: ['c', 'd', 'e', 'f', 'a']
def rotation_point(rotated_list):
  #start with low, high, and min values
  low = 0
  high = len(rotated_list) - 1 #length 1 greater than index
  while low <= high:
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list) #make sure that indices are in list length
    mid_previous = (mid - 1) % len(rotated_list)
    
    if (rotated_list[mid] < rotated_list[mid_previous]) and (rotated_list[mid] < rotated_list[mid_next]):
      #if rotated_list[mid] is less than both values around it, it is the target index
      return mid
    elif rotated_list[mid] < rotated_list[high]:
      #if not, check if right is sorted. If so, ignore it and decrement high to mid - 1
      high = mid - 1
    else:
      #else, left is sorted. Ignore left and increment low to mid + 1
      low = mid + 1


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))