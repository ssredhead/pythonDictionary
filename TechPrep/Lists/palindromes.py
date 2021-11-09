# How would you write a function that checks if a string is a palindrome?
# 1) Clarify the question: Palindrome = opposite indexes are the same value
#   Questions and assumptions?
#   Does capitalization and/or spaces matter?
#   Can we assume this is an alphabet, or a Unicode/ASCII situation? Special Characters, numbers, etc.
#   Are any data types or function types restricted?
# 2) Create Inputs
#   "aba" or "abba" # "simple" palindromes
#   "taco cat" # palindrome with spaces
#    "racecar!" # palindrome with punctuation
#   "able was I, ere I saw elba" # both!
# 3) Outline the solution:
#   Approach 1: A recursive or iterative function that compares the first and last index
#   And then iterates/recurses with the remaining string, minus the first and last indexes
#   return true if the pattern matches, false if it doesn't
# 4) Code the solution

def palidrome(p_str):
    #base case 1 - if string is 0, 1 char, it is a palidrome
    if len(p_str) <= 1:
        return True
    #base case 2 - If the first and last indexes do not have matching characters, it is not a palidrome
    if p_str[0] != p_str[-1]:
        return False
    
    return palidrome(p_str[1, -1]) #recurse with p_str from index 1 to the second to last index, because range is not inclusive

#What if we can't use recursion? (which has a high space complexity and is bad for large inputs)
def palidrome_2(p_str):
    #if string is 0, 1 char, it is a palidrome
    if len(p_str) <= 1:
        return True
    for i in range(len(p_str) // 2):
        if p_str[i] != p_str[-i - 1]: #We only need to go through half of the array because of the subracting from the last index
            return False
    #if the for loop ends and False has not been returned, all characters match, it is a palidrome
    return True

#What if we don't care about capitalization?
def palidrome_3(p_str):
    lower = p_str.lower()
    #if string is 0, 1 char, it is a palidrome
    if len(lower) <= 1:
        return True
    for i in range(len(lower) // 2):
        if lower[i] != lower[-i - 1]: #We only need to go through half of the array because of the subracting from the last index
            return False
    #if the for loop ends and False has not been returned, all characters match, it is a palidrome
    return True

# what if we wanted to ignore punctuation?
def palindrome_4(p_str):
  punctuation = [',', '!', '?', '.']
  no_punc_str = p_str[:]
  for punc in punctuation:
    no_punc_str = no_punc_str.replace(punc, '')
  for i in range(len(no_punc_str) // 2):
    if no_punc_str[i] != no_punc_str[-i - 1]:
      return False
  return True 

# what if we wanted to ignore space?
def palindrome_5(p_str):
  no_space_str = p_str.replace(' ', '')
  for i in range(len(no_space_str) // 2):
    if no_space_str[i] != no_space_str[-i - 1]:
      return False
  return True 

# 5) Test the solution:
# With each of these different functions, different tests pass, 
# since we ignore different kinds of characters with each
# 6) Analyze the solution:
#   All of these have runtime less than O(n) where n is the length of the string,
#   because we decrease interaction with the string each time
#   In this case, the iterative implementation is more efficient, because it has O(1) space complexity.

