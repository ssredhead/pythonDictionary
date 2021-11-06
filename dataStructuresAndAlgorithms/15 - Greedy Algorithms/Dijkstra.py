# Dijkstra’s Algorithm works as following:

# Instantiate a dictionary that will eventually map vertices to their distance from the start vertex
# Assign the start vertex a distance of 0 in a min heap
# Assign every other vertex a distance of infinity in a min heap
# Remove the vertex with the smallest distance from the min heap and set that to the current vertex
# For the current vertex, consider all of its adjacent vertices and calculate the distance to them as (distance to the current vertex) + (edge weight of current vertex to adjacent vertex).
# If this new distance is less than the current distance, replace the current distance.
# Repeat 4 and 5 until the heap is empty
# After the heap is empty, return the distances

# In the worst case, we would update the min-heap every iteration. 
# Since there are at most E + V iterations of Dijkstra’s and it takes log V 
# to update a min-heap in the worst case, then the runtime of Dijkstra’s is O((E+V)log V).

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }

def dijkstras(graph, start):
  distances = {} #keep track of all shortest distances
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore) #this will always be the vertex with the min distance from start

    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))

  return distances
