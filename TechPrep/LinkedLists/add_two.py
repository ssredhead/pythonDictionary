from linked_list import LinkedList, Node, build_test_case

linked_list_a, linked_list_b = build_test_case()

# Each node in a linked list holds the digit of a number. 
# The tail node holds the most significant digit and the head node holds the least significant digit.

# 2 -> 4 -> 1
# represents the number 142
# 7 -> 1
# represents the number 17

# Given two of these linked lists, write a function that 
# returns the sum of the two numbers as a new linked list.

# 2 -> 4 -> 1
# plus
# 7 -> 1
# returns
# 9 -> 5 -> 1

# return an instance of LinkedList which contains the sum of the input linked lists.

def add_two(linked_list_a, linked_list_b):
  #traverse both lists simultaneously
  #add the values found at each head node
  #store the result at a new Node instance
  result = LinkedList()
  carry = 0 #contains the overflow if adding two digits sums greater than 9
  a_node = linked_list_a.head
  b_node = linked_list_b.head

  while a_node or b_node: #continue until longer list ends
    #check if each node exists before adding
    if b_node:
      b_val = b_node.val
      print("b_val")
      print(b_val)
      b_node = b_node.next #move next
    else:
      b_val = 0 #placeholder, won't effect sum

    if a_node:
      a_val = a_node.val
      print("a_val")
      print(a_val)
      a_node = a_node.next #move next
    else:
      a_val = 0 #placeholder, won't effect sum
    
    #add sums together along with the carry
    to_sum = a_val + b_val + carry
    print("to_sum")
    print(to_sum)
    #ideally to_sum is a single digit, but if it is above 9, retrieve a single digit using the % operator along with 10 (decimal)
    #ex 15 % 10 = 5 carry = 1
    if to_sum > 9:
      carry = 1
      to_sum %= 10
    else:
      carry = 0
    #set up return value without .add() because it is reverse order
    #check if we have an existing result head or create one if it does not exist.
    if not result.head:
      result.head = Node(to_sum)
      print("head")
      print(result.head.val)
      temp = result.head
    else:
    #use a temp tracker to track trail node of result as it is being built out
      temp.next = Node(to_sum) #the "current" value before to_sum node is added
      print("next")
      print(temp.val)
      temp = temp.next #temp is now the to_sum node (i.e. it has been added)
    
    #there might be a remaining carry at the end. Add it if it exists
    if carry:
      temp.next = Node(carry) #add final node that is equal to carry
    
    print("result")
    print(result)
  return result


print("Adding linked list:\n{0}\nto linked list\n{1}\n".format(linked_list_a, linked_list_b))
result = add_two(linked_list_a, linked_list_b)
print("Result should be: 9 -> 5 -> 1 ->\nFunction returned:\n{0}".format(result))

#Output with test print statements:

# Adding linked list:
# 2 -> 4 -> 1 -> 
# to linked list
# 7 -> 1 -> 

# b_val = 7
# a_val = 2
# to_sum = 9
# head = 9
# result = 9 -> 

# b_val = 1
# a_val = 4
# to_sum = 5
# next = 9
# result = 9 -> 5 -> 

# a_val = 1
# to_sum = 1
# next = 5
# result = 9 -> 5 -> 1 -> 

# Result should be: 9 -> 5 -> 1 ->
# Function returned:
# 9 -> 5 -> 1 -> 