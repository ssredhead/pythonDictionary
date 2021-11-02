def fibonacci(n):
  #append subsequent fibs numbers, return the last
  fibs = [0, 1]
  if n < 0:
    ValueError("Input 0 or greater only!")

  if n <= len(fibs) - 1:
    return fibs[n]
  
  while n != 1:
    #add previous two indexes for new number
    fibs.append(fibs[-1] + fibs[-2])
    n -= 1
  #return final number
  return fibs[-1]

  # test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)

#recursive implementation
# runtime: Exponential - O(2^N)
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)