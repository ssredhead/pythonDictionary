# pair sum
# linear time, linear space requirement
# return list of indices that sum to target

# If we sort the list before looking for pairs, 
# we can reach O(N * logN) time complexity, 
# but we’re going to go for a O(N) solution by trading away a little space.

# As with other naive solutions, we’re doing more work than is necessary. 
# Given the target integer, what information we can gather in a single iteration?

# <> marks the current element
# nums = [4, 2, 8, 9, 6]
# target = 8
 
# [<4>, 2, 8, 9, 6]
# target - 4 = 4
# we need another 4...
 
# [4, <2>, 8, 9, 6]
# target - 2 = 6
# we need a 6...
 
# [4, 2, <8>, 9, 6]
# target - 8 = 0
# we need a 0...
 
# [4, 2, 8, <9>, 6]
# target - 9 = -1
# we need a -1...
 
# [4, 2, 8, 9, <6>]
# target - 6 = 2
# we need a 2...

# At each step of the iteration, we know the “complement” number needed to sum to the target.

#Use a dictionary to store that complement at each iteration 
# and solve this problem with O(N) time complexity and O(N) space complexity.

def pair_sum(nums, target):
  complements = {} #keeps track of complementary values
  indices = {} #keeps track of indices to be returned
  for i in range(len(nums)):
    val = complements.get(nums[i], None) #try to get complement with a None default value
    if val is not None: #if the val is there, return the current index and the index of val in indices
      return [indices[val], i] #ex indices[2] = 0, i = 4 where 8 - 2 = 6
    complements[target - nums[i]] = nums[i] #if not, subtrack current val from target, use that as the dict key, and make the index value the value
    indices[nums[i]] = i #use current value as key, index as value for indices dict
  return None #if pair not found, return 0

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([1, 2, 3, 4, 5], 6), [[1, 3], [0,4]], pair_sum([1, 2, 3, 4, 5], 6) in [[1, 3], [0,4]]))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21), [[5, 6]], pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21) in [[5, 6]]))

print("{0}\n should equal \n{1}\n {2}\n".format(pair_sum([1, -7, 2, 15, -11, 2], 42), None, pair_sum([1, -7, 2, 15, -11, 2], 42) == None))

print("{0}\n should equal any of \n{1}\n {2}\n".format(pair_sum([0, -7, 2, 15, -11, 2], 2), [[0, 2], [0,5]], pair_sum([0, -7, 2, 15, -11, 2], 2) in [[0, 2], [0, 5]]))