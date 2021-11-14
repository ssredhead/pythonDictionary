num_in_fibonacci = 11
function_calls = []

# The Fibonacci sequence is a perfect case to apply dynamic programming. 
# Each Fibonacci number relies on two previous numbers, and those numbers never change.
# We have overlapping sub-problems!

# We’ll store the answers to sub-problems using memoization. 
# Think of it like jotting notes down on a memo.

# With each sub-problem, we’ll check if we have a note in our memo. 
# If we do, then we can use that information, otherwise, we’ll need to do a calculation 
# and then store that calculation in our memo pad!

# Just like the 1 + 1 + 1 + 1 example, we don’t need to recompute the 3rd and 4th Fibonacci 
# number to calculate the 5th Fibonacci number if we already know the 3rd and 4th number.

def fibonacci(num, memo):
  function_calls.append(1)
  if num < 0:
    print("Not a valid number")
  if num <= 1:
    return num
  elif memo.get(num): #if the fib calculation is already in memo, just return it
      return memo.get(num)
  else: #if not, calculate it and store it in memo
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]
  
  
fibonacci_result = fibonacci(num_in_fibonacci, {})
print("Number {0} in the fibonacci sequence is {1}.".format(num_in_fibonacci, fibonacci_result))

print("Fibonacci function called {0} total times!".format(len(function_calls)))

#Output:
# Number 11 in the fibonacci sequence is 89.
# Fibonacci function called 21 total times!