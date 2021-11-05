#Graph
# Can be initialized as a directed graph, where edges are set in one direction.
# Stores every vertex inside a dictionary
# Vertex data is the key and the vertex instance is the value.
# Has methods to add vertices, edges between vertices, and determine if a path exists between two vertices.

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    #make dictionary to track vertices:
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      #If current_vertex has been seen add it to dictionary:
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        
        # Filter next_vertices so it only
        # includes vertices NOT IN seen
        
        # continue as long as vertex has not already been seen:
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        start.extend(next_vertices)
        
    return False
