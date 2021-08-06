#This is an optimized way of finding out whether a number is prime
#Since all prime numbers besides 2, and 3 can be expressed in the form 6k +- i
# For some integer k and for i = -1, 0, 1, 2, 3, or 4
for _ in range(int(input())):
    num = int(input())
    if num == 1:
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(num**(1/2))+1, 2): #using 6k +- 1 optimization
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")