from TreeNode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=()):
  path = path + (root,) #build path as a tuple (immutable)

  if root.value == target:
    return path #return tuple path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None
        
node = dfs(sample_root_node, "F")
print(node)