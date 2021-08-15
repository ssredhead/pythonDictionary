def max_num(first, second, third):
  if (first > second and first > third):
    return first
  elif (second > first and second > third):
    return second
  elif (third > first and third > second):
    return third
  else:
    return "It's a Tie!"

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
