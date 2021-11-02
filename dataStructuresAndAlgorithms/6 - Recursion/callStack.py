def sum_to_one(n):
  result = 1
  call_stack = []
  
  #simulates recursive calls to reach base case
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  #simulates execution_context/solving of recursion
  while len(call_stack) != 0 :
    return_value = call_stack.pop()
    print(call_stack)
    print("Adding " + str(return_value["n_value"]) + " to result")
    result += return_value["n_value"] 
  return result, call_stack

sum_to_one(4)