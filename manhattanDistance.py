#Manhattan distance is always >= Euclidean distance.

def manhattan_distance(pt1, pt2):
  distance = 0

  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

print(manhattan_distance([1, 2], [4, 0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))