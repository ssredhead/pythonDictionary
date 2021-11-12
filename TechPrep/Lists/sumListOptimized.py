# max sub sum
# linear time, constant space requirements
# return maximum contiguous sum in list

# optimize using an important concept: 
# We don’t always need to create every possible outcome to know what’s best.

# Do we need to make every sub-list? 
# No! 
# We can visit each value within the list and keep a running tally of sums.

# # <> will mark the current element
# nums = [1, -7, 2, 15, -11, 2]
# most_seen = 0
# current_max_sub_sum = 0
 
# [<1>, -7, 2, 15, -11, 2]
# most_seen = 1
# current_max_sub_sum = 1
 
# [1, <-7>, 2, 15, -11, 2]
# most_seen = 1
# current_max_sub_sum = -6
 
# our sum is negative
# anything positive which comes after
# will be better without this "sub-list"
# reset current max to 0!
 
# current_max_sub_sum = 0
 
# [1, -7, <2>, 15, -11, 2]
# most_seen = 2
# current_max_sub_sum = 2
 
# [1, -7, 2, <15>, -11, 2]
# most_seen = 17
# current_max_sub_sum = 17
 
# [1, -7, 2, 15, <-11>, 2]
# most_seen = 17
# current_max_sub_sum = 6
 
# # current sum went down, but not negative
# # no need to reset!
 
# [1, -7, 2, 15, -11, <2>]
# most_seen = 17
# current_max_sub_sum = 8

def maximum_sub_sum(my_list):
    if max(my_list) < 0:
      return max(my_list) #if the highest value in my_list is negative, just return it
    
    max_sum = 0 #sum to be returned
    max_sum_tracker = 0 #current consecutive sum

    for i in range(len(my_list)):
        max_sum_tracker += my_list[i] #add next consecuritve value to tracker
        if max_sum_tracker < 0: #if value is negative, no need to continue, reset max_sum_tracker
            max_sum_tracker = 0
        if max_sum_tracker > max_sum: #if it is higher than current max_sum, replace it
            max_sum = max_sum_tracker
    return max_sum

# linear time, constant space requirements


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, 2, 3, 4, 5]), 15, maximum_sub_sum([1, 2, 3, 4, 5]) == 15))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]), -1, maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]) == -1))

print("{0}\n should equal \n{1}\n {2}\n".format(maximum_sub_sum([1, -7, 2, 15, -11, 2]), 17, maximum_sub_sum([1, -7, 2, 15, -11, 2]) == 17))