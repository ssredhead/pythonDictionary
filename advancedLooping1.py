#Return greater sum of list given 2 lists
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0

  for i in lst1:
    sum1 += i
  for j in lst2:
    sum2 += j
  
  if sum1 >= sum2:
    return sum1
  return sum2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
