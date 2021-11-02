# Data structures, like binary search trees can be recursive, too
#"left" child < "parent" node < "right" child

def build_bst(my_list):

  #base case: leaf node
  if my_list == []:
    return "No Child"

  #divide list in half:
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print("Middle index: {}".format(middle_idx))
  print("Middle value: {}".format(middle_value))

  #implement bst with dictionary
  #repeate this process on the left and right sub-trees
  tree_node = {"data": middle_value}
  #recursive calls to subtrees:
  tree_node["left_child"] = build_bst(my_list[:middle_idx]) #not including middle_idx
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1:]) #not including middle_idx
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN" #logN for sort algorithm, N for appending all values


#output
# Middle index: 2
# Middle value: 14
# Middle index: 1
# Middle value: 13
# Middle index: 0
# Middle value: 12
# Middle index: 1
# Middle value: 16
# Middle index: 0
# Middle value: 15
# {'data': 14, 
# 'left_child': { 
# 'data': 13, 
# 'left_child': { 'data': 12, 
# 'left_child': 'No Child', 
# 'right_child': 'No Child'}, 
# 'right_child': 'No Child'}, 
# 'right_child': {
# 'data': 16, 
# 'left_child': {'data': 15, 
# 'left_child': 'No Child', 
# 'right_child': 'No Child'}, 
# 'right_child': 'No Child'}
# }