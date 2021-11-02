def merge_sort(items):
  #base case
  if len(items) <= 1:
    return items
  #split remaining array
  middle_index = len(items) // 2
  #not including middle_index (not inclusive)
  left_split = items[:middle_index]
  #includes middle_index
  right_split = items[middle_index:]

    #recurse the splitting to break down sublists
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  #recurse the actual sorting and merging
  return merge(left_sorted, right_sorted)

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)
print(ordered_list1)
print(ordered_list2)
print(ordered_list3)

def merge(left, right):
  result = []
  #keep going while left and right aren't empty 
  while left and right:
    if left[0] < right[0]:
      result.append(left[0])
      #once the smallest value is appened to result, pop it off of left
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

    #if there are any left items remaining, tack them onto result
  if left:
    result += left
  elif right:
    result += right

  return result
