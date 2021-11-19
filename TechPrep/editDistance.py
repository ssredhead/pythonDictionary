string_1 = "cat"
string_2 = "bat"
string_3 = "bar"
string_4 = "at"
string_5 = "cats"

def edit_distance(string_1, string_2):
    set_1 = set(string_1)
    set_2 = set(string_2)

    print(set_1)
    print(set_2)

    edits = set_1 - set_2
    return len(edits)

print(edit_distance(string_1, string_2))
print(edit_distance(string_1, string_3))
print(edit_distance(string_2, string_3))
print(edit_distance(string_1, string_4))
print(edit_distance(string_1, string_5))
print(edit_distance(string_2, string_5))
