#Given a list of strings, find the maximum length of a subtring with all unique characters from the string

def max_length(lst):
    if len(lst) <= 1:
        return len(lst)

    char_str = ''.join(lst)
    print(char_str)
    unique_set = set(char_str)
    print(unique_set)

    return len(unique_set)

print(max_length(["ab", "bc", "ax","qz", "rs"]))

def max_length_2(lst):
    if len(lst) <= 1:
        return len(lst)
    
    char_str = ''.join(lst)
    
    unique_dict = {}
    for letter in char_str:
        if letter not in unique_dict:
            unique_dict[letter] = True
    
    return len(unique_dict)

print(max_length_2(["ab", "bc", "ax","qz", "rs"]))

def remove_dupes(str_input):
    unique_set = set(str_input)
    str_input = str(unique_set)
    return str_input

print(remove_dupes("supercalifragilisticexpialidocious"))