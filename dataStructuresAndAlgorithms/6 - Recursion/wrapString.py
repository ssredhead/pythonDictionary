# define wrap_string()
#string is the string you want to wrap
#n is the number of "<" and ">" you want to wrap it in
def wrap_string(string, n):
  result = ""
  if n <= 0:
    return string
  result += "<"
  result += wrap_string(string, n - 1)
  result += ">"

  return result

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)