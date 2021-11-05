def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0) #remove from front bc FIFO
    visited.add(current_vertex)
    #graph[current_vertex] holds references to the neighboring vertices
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor == target_value:
          #add neighbor to path before returning
          return path + [neighbor]
        else:
          #remember to add neighbor to the path
          bfs_queue.append([neighbor, path + [neighbor]])

# Call bfs() below and print the result:
print(bfs(the_most_dangerous_graph, 'crocodiles', 'bees'))