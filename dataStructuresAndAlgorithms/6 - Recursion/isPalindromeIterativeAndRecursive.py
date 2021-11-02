def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  #if the first char != the last char
  if my_string[0] != my_string[-1]:
    return False 
  #if they match, recurse with the second char and the second to last char (because range is not inclusive)
  return is_palindrome(my_string[1:-1])
    


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)

#Iterative implementation
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 