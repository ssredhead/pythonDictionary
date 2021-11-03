from tree import TreeNode
from bfs import breadthFirstSearch

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
# Change the 2nd argument below
goal_path = bfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)

#Output:
# |-Documents
# | |-WishList.txt
# | |-TodoList.txt
# |-Photos
# | |-Fluffy.jpg
# | |-Spot.jpg

# Searching node with value: Home
# Searching node with value: Documents
# Searching node with value: Photos
# Searching node with value: WishList.txt
# Searching node with value: TodoList.txt
# Searching node with value: Fluffy.jpg
# Path found
# Home
# Photos
# Fluffy.jpg