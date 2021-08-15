def in_range(num, lower, upper):
  i = lower
  for i in range(lower, upper+1):
    if num == i:
      return True
    i += 1
  return False


print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
