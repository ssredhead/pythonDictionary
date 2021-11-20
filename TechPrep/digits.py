#two inputs 1 = # of digits
#2 = base of the number system
#output = all of the numbers that can be created in that base system with the number of digits specified

#Clarifying Questions:
#bases = 10, 2, 16, etc. 

# 3 digit number of base 2 = [000, 111, 110, 011, 101, 001, 100]

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