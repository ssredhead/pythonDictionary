from util import powerset, Loot

def knapsack(loot, weight_limit):
  best_value = None
  all_combo = powerset(loot) #all possible combos
  for combo in all_combo: #for the list of items made by powerset in each combo
    combo_weight = sum([item.weight for item in combo]) #get the list's total weight list comprehension
    combo_value = sum([item.value for item in combo]) #get list's total value list comprehension
    if combo_weight <= weight_limit: #if the list's weight fits in the weight limit
      if best_value == None or combo_value > best_value: #if it is better than best value
        best_value = combo_value #reassign best_value

  if best_value == None:
    print("knapsack couldn't fit any items")
  return best_value
    
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))