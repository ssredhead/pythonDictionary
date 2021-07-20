#making a dictionary with a user's first name and phone number
phonebook = {}
entries = int(input())

for n in range (entries):
    name, num = input().strip().split(' ') #parse input string
    name, num = [str(name), int(num)] #cast input to desired data types
    phonebook[name] = num #assign key-value pair to dictionary

    while True:
            try:
                search = str(input())

                if search in phonebook:
                    output = ''.join('%s=%r' % (search, phonebook[search]))
                    print(output)
                else:
                    print("Not found")
            except EOFError:
                break
