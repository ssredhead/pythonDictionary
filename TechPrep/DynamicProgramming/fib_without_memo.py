
num_in_fibonacci = 11
arguments_count = {}

def fibonacci(num):
  count = arguments_count.get(num, 0) #get count as key of dictionary "num" with 0 as default because sometimes a key won't exist
  count += 1
  arguments_count[num] = count
  if num < 0:
    print("Not a valid number")
  if num <= 1:
    return num
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)
  

print("Number {0} in the fibonacci sequence is {1}.".format(num_in_fibonacci, fibonacci(num_in_fibonacci)))
      
for num, count in arguments_count.items():
  print("Argument {0} seen {1} time(s)!".format(num, count))

print("Fibonacci function called {0} total times!".format(sum(arguments_count.values())))

#Output: This illustrates how many values are repeatedly called over the course of the function
#In fact, as each number decreases, it is a direct correlation to the fib sequence.

# Number 11 in the fibonacci sequence is 89.
# Argument 11 seen 1 time(s)!
# Argument 10 seen 1 time(s)!
# Argument 9 seen 2 time(s)!
# Argument 8 seen 3 time(s)!
# Argument 7 seen 5 time(s)!
# Argument 6 seen 8 time(s)!
# Argument 5 seen 13 time(s)!
# Argument 4 seen 21 time(s)!
# Argument 3 seen 34 time(s)!
# Argument 2 seen 55 time(s)!
# Argument 1 seen 89 time(s)!
# Argument 0 seen 55 time(s)!
# Fibonacci function called 287 total times!