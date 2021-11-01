class Node:
    #init function always has self. Link_node is by default none (they are unconnected nodes)
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
    #self is always included in getter and setter calls
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

#yacko can keep track of dot
yacko.set_link_node(dot)
#dot can keep track of wacko
dot.set_link_node(wacko)

#gets dot's value by getting the link from yacko and then it's value
dots_data = yacko.get_link_node().get_value()
#same for wacko. i.e. yacko(value | link) -> dot(value | link) -> wacko(value | link) -> null
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)
#gets yacko's value
print(yacko.get_value())
#gets wacko's value from yacko, via dot
print(yacko.get_link_node().get_link_node().get_value())