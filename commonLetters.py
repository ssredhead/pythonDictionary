#This function takes two strings and returns a list of unique shared characters
def common_letters(string_one, string_two):
  common = []
  for o in string_one:
    if o in string_two:
      if o in common:
        continue
      common.append(o)
  return common
