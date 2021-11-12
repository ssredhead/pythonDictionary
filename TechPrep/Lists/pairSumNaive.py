# pair sum
# no time/space requirements
# return list of indices that sum to target

# Clarifying Questions:

# Are there constraints on time or space efficiency?
# No! Any solution will do.
# Can the numbers be negative or 0?
# Yes! Your solution should handle those inputs.
# Does the order of indices matter?
# The earlier index comes first in the return list.
# Do we return all pairs that match a solution?
# No! The first one that your solution finds will do!

def pair_sum(nums, target):
  for i in range(len(nums)): 
    for j in range(i, len(nums)): #range within original loop, don't repeat the i index
      if nums[i] + nums[j] == target:
        return [i, j] #return the pair as an array
  return None

#O(n^2) because we loop through the list twice, each n times

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([1, 2, 3, 4, 5], 6), [[1, 3], [0, 4]], pair_sum([1, 2, 3, 4, 5], 6) in [[1, 3], [0,4]]))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21), [[5, 6]], pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21) in [[5, 6]]))

print("{0}\n should equal \n{1}\n {2}\n".format(pair_sum([1, -7, 2, 15, -11, 2], 42), None, pair_sum([1, -7, 2, 15, -11, 2], 42) == None))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([0, -7, 2, 15, -11, 2], 2), [[0, 2], [0,5]], pair_sum([0, -7, 2, 15, -11, 2], 2) in [[0, 2], [0, 5]]))