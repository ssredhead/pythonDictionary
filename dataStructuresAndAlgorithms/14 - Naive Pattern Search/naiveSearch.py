def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0

    for char in range(len(pattern)):
      print("Pattern Index:", char)
      
      if pattern[char] == text[index + char]: #backtracking section. Emmulates a mini loop through text without actually iterating
        print("Matching index found")
        print("Match Count:", match_count)
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)

#Output
# Input Text: HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE Input Pattern: NEEDLE
# Text Index: 0
# Pattern Index: 0
# Text Index: 1
# Pattern Index: 0
# Text Index: 2
# Pattern Index: 0
# Text Index: 3
# Pattern Index: 0
# Text Index: 4
# Pattern Index: 0
# Text Index: 5
# Pattern Index: 0
# Text Index: 6
# Pattern Index: 0
# Pattern Index: 1
# Pattern Index: 2
# Pattern Index: 3
# Pattern Index: 4
# Pattern Index: 5
# NEEDLE found at index 6
# Text Index: 7
# Pattern Index: 0
# Text Index: 8
# Pattern Index: 0