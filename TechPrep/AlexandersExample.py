#BFS is best for determining the best path from one node to another
#queue of nodes on each level/distance, determining if they are connected to the node you see currently
#marking them as visisted or checked out in some way
#expands from the node you found longest ago (LIFO)
#Takes an edge from the most recently found node

#DFS best used for determining the completeness of a graph or a tree,
# uses a stack to determine the level/tracking 
# and/or determing whether or not one node is connected to another
#expands from the node you found most recently (FIFO)

# BFS: take an edge from the node added to S most recently.
# DFS: take an edge from the node added to S least recently.
# Prim: Take the edge with the minimum weight.
# Dijkstra: Take an edge from the vertex closest to s.

#Priority Queue - a queue where an element has two attributes (to determine when it will leave)
#1) Priority (higher or lower) pick the highest priority
#2) Time into the queue (FIFO)

#Implement a priority queue

#Approach 1, more visually
priorityQueue = [
    {
        'name': "Jiles",
        'time': "now",
        'priority': "High"
    },

    {
        'name': "Charlie",
        'time': "now",
        'priority': "Low"
    }
]

#Find a shortest path from the red dot to the green (if one exists)
#The grey spaces are inaccessible
#The cardinal directions, and diagonals are all possible directions

#Given: A grid (matrix) 
#Return: a shortest path, or a string that a path doesn't exist

#Main function that checks whether the grid is valid and kick off the recursive 

#A Star - Informed Algorithm. It is targeted (looks to the future and looking for one node)
#Potentially does a lot less work because it is only looking for the green dot.
#Two costs (uses priority queue) - piority value is the key is f(n) = g(n) + h(n) 
# where n = node, g(n) is the travelers cost to the current best option
#h(n) the heuristic cost, a guess at how far n is from g (goal node) 
# how far do I have to get to that node? How far is that node from what I want?
# s (start node) gets pushed onto the priority queue to init


#BFS - Blind. Just opens the next node in the queue
#Dijkstra's - Based on distance previously travelled. Not targeted (finds every node)

#Based on the graph, our movement options are limited.
#A relaxed (heuristic) approach might be a straight line or through grey squares.
#The most relaxed approach is: Find a straight line path between these points
#Your heuristic has the characteristic "admissibility" if it is at worst optimistic and at best realistic.
#It can never be pessimistic (giving an expected cost that is greater than the actual cost)
#The second characteristic is "consistency" if it is realistic for all paths to g that can originate from n

#This means that with this heuristic, the algorithm will prefer 
# to open nodes that it thinks will be closest to the goal node
# meaning it will avoid extra work based on its assumptions.
# If it's a good heuristic, the algorithm will make choices like the optimal path (close to the actual cost)

#Any time algorithm - can be stopped any time after an initial runtime and will return some answer
#It will store an answer and then continue to search for a better answer.
#Stopping this algorithm will return the best solution it currently has.

#Adjacency lists - used to store graphs (preferred for large, sparse graph)

#Priority queues are implemented with a heap. The key values for the priority inform the heap
