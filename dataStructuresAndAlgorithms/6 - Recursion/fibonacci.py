#fibonacci() is an example of multiple recursive calls
#complexity O(2^n) where n is the number of recursive calls in each process

#the next fib number is the sum of the previous two fib numbers
def fibonacci(n):
  print(n)
  #base cases:
  if (n == 1) or (n == 0):
    return n
  #recursive case:
  return fibonacci(n - 1) + fibonacci(n - 2)




fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = '2^N'