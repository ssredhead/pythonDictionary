dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
  #each string will represent the row/colum of a grid, like the knapsack problem
  #remember to add an extra row and column to just hold the empty string or "no character"
  grid = [[0 for row in range(len(string_1) + 1)] for col in range(len(string_2) + 1)]
  #in a nested for loop, compare each letter from one string with each of another
  for row in range(1, len(string_2) + 1):
    print("Comparing: {0}".format(string_2[row - 1]))
    for col in range(1, len(string_1) + 1):
      print("Against: {0}".format(string_1[col - 1]))
      if string_1[col - 1] == string_2[row - 1]:
        #these letters match and there is a subsequence of at least 1 (maybe more)
        #those matches live at grid[row - 1][col - 1] 
        #add 1 to the previous matches
        grid[row][col] = grid[row - 1][col - 1] + 1
      else: 
        #they don't match
        #fill the current space with the best we've seen excluding either character (i.e. the value located at the prior row or column)
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
  
  for row_line in grid:
    print(row_line)
  return grid[-1][-1] #last index holds best value

longest_common_subsequence(dna_1, dna_2)

#O (N * M) implementation

#Output:
# Finding longest common subsequence of ACCGTT and CCAGCA
# Comparing: C
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# Comparing: C
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# Comparing: A
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# Comparing: G
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# Comparing: C
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# Comparing: A
# Against: A
# Against: C
# Against: C
# Against: G
# Against: T
# Against: T
# [0, C, C, A, G, C, A] #all the letter places actually hold "0"
# [A, 0, 1, 1, 1, 1, 1]
# [C, 0, 1, 2, 2, 2, 2]
# [C, 1, 1, 2, 2, 2, 2]
# [G, 1, 1, 2, 3, 3, 3]
# [T, 1, 2, 2, 3, 3, 3]
# [T, 1, 2, 2, 3, 3, 3] <- highest value