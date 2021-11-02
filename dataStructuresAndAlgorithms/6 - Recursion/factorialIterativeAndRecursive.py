def factorial(n):
  result = 1
  if n < 0:
    ValueError("Inputs 0 or greater only")
  while n != 0:
    result *= n
    n -= 1
  return result


# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

#recursive version
# runtime: Linear - O(N)
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)