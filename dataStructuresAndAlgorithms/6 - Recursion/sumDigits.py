def sum_digits(n):
  if n < 10:
    return n
  else:
    last_digit = n % 10
    # n//10 gets every element but the last one (150 // 10 = 15)
    return last_digit + sum_digits(n // 10)
  
print(sum_digits(12))
# 3
print(sum_digits(194))
# 14

#iterative implementation
# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n