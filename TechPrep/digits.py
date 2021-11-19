#two inputs 1 = # of digits
#2 = base of the number system
#output = all of the numbers that can be created in that base system with the number of digits specified

#Clarifying Questions:
#bases = 10, 2, 16, etc. 

# 3 digit number of base 2 = [000, 111, 110, 011, 101, 001, 100]

def base_combinations(digits, base):

    #define the digits available in the bases
    possible_numbers = set(range(0, base)) #base 2 0,1

    total_numbers = set() 

    #calculate the permutations of the possible numbers for as many digits
    #build a number out the possible numbers up until they are they are the length that we choose
    count = 0
    new_num = 0
    while count < digits:
        for num in possible_numbers:
            new_num.append(num)

        count += 1

    if new_num in total_numbers:
        pass
        
    else:
        total_numbers.add(new_num)

    return total_numbers


def base_of_size(base, size):
    def recurse(res, row, i=0):
        if i >= size:
            res.append(row[:])
        else:
            for j in range(base):
                row[i] = j
                recurse(res, row, i + 1)

        return res

    return recurse([], [None] * size)

print(base_of_size(2, 10))