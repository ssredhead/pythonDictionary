from util import Loot

# Just like with Fibonacci, we’re repeating computations that won’t change.

# With the Fibonacci Sequence, we had one variable to store: the number itself. 
# We could place that number in a Python dictionary and look it up as needed.

# Now we’re dealing with multiple variables: 
# the item’s weight and value as well as the capacity of the knapsack. 
# A dictionary’s key-value pairs won’t be sufficient to store all the answers to our subproblems.

# We’ll start tackling this problem by building a grid which can store all our sub-answers.

# The columns of our grid represent each possible capacity up to the weight limit.

# The rows of our grid represent each possible item we can fit into a knapsack.

# Why do we want each possible capacity? 
# Because finding the optimal capacity for a knapsack of weight 4 will be much more efficient 
# if we already know the optimal capacities for knapsacks of weight 3 and 1.

# each column is the capacity of a knapsack and each row is an item we can add. 
# The first row is “no item” and the first column is “no capacity”

def knapsack(loot, weight_limit):
  #two dimensional list/matrix [loot][weight]
  #two nested list comprehensions build this soltion:
  grid = [[0 for column in range(weight_limit + 1)] for row in range(loot = 1)] # + 1 because 0 weight is accounted
  #populate the grid with values by iterating through each item in loot
  #use enumerate(loot) to access row (index) and item (loot instance/column)
  for row, item in enumerate(loot):
    row = row + 1
    #for each item, consider how they fit into all of the sub-knapsacks
    for col in range(weight_limit + 1):
      #loop through each col -- each index is also the weight capacity (i.e. col 2 represents knapsack capacity 2)
      weight_capacity = col
      if item.weight <= weight_capacity:
        item_value = item.value
        item_weight = item.weight
        #we have two options: 
        #1) item + value stored at remaining weight
        previous_best_less_item_weight = grid[row - 1][weight_capacity - item_weight]
        capacity_value_with_item = item_value + previous_best_less_item_weight
        #2) the previous best in the weight capacity
        capacity_value_without_item = grid[row - 1][col]
        #set current grid space to larger of these two values
        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        #if the item weight doesn't fit, set the grid space to the best value for the previous weight
        grid[row][col] = grid[row - 1][col]
  #return bottom-right section of grid (best value)
  return grid[len(loot)][-1]
    
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))

# We’ll consider the diamond first. 
# It weighs 1 pound and is worth $7. 
# For each capacity after 0 (our first column), we can place the diamond in that location. 
# Some capacities have spare weight, but that’s okay.

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# Let’s add a trophy worth $6 and weighing 2 lbs.

# The trophy doesn’t fit in a 1lb. knapsack, so we look at the previous row 
# and fill this section with that value.

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, (7), 7, 7, 7]
# third row: Trophy   [0, (7), ?, ?, ?]
# The trophy fits in the 2lb. knapsack; we have two options:

# Trophy plus value stored at the remaining weight
# The previous best in the 2lb. sub-knapsack.
# Adding the 2 lb. trophy would mean 0 remaining capacity. 
# This is why “no capacity”, “no item” values live in our grid.

# Option 1 = 6 (trophy value) + 0 (“no capacity” value)

# Option 2 = 7 (the previous best)

# By weighing our options, 
# we see this section should store the diamond value even though there’s spare weight. 
# We’re maximizing for value!

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, ?, ?]
# We repeat this process with the 3lb. sub-knapsack:

# Option 1 = 6 (trophy value) + 7 (1lb. sub-knapsack value) Option 2 = 7 (the previous best)

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, 13, ?]
# One last time for the 4lb. knapsack:

# Option 1 = 6 (trophy value) + 7 (2lb. sub-knapsack value) Option 2 = 7 (the previous best)

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Diamond [0, 7, 7, 7, 7]
# third row: Trophy   [0, 7, 7, 13, 13]
# Note that the best value is stored in our bottom-right section. 
# This is true no matter how many items we add.

# The order we consider items is irrelevant for the final value. 
# Here’s how the grid would look trophy-first:

           # Capacity: 0| 1| 2| 3| 4|
#____________________________________
# first row: no item! [0, 0, 0, 0, 0]
# second row: Trophy  [0, 0, 6, 6, 6]
# third row: Diamond  [0, 7, 7, 13, 13]