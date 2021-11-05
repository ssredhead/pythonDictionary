# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    #use max and min functions
    m = max(A) #6
    print("max: " + str(m))
    if m < 1:
        return 1 #all values are negative
    
    #take the intersection of the following sets to get answer
    set_A = set(A) #[1,2,3,4,6]
    print("set_A: ")
    print(set_A)
    set_B = set(range(1, m + 1)) #[1,2,3,4,5,6] a simple range that goes from 1 to the max number in the list (range not inclusive so +1)
    print("set_B: ")
    print(set_B)
    set_C = set_B - set_A #[5] #subract them
    print("set_C: ")
    print(set_C)
    if len(set_C) == 0:
        return m + 1 #meaning max is 0, return 1
    return min(set_C) #there may be more than one element in set_C, so return the smallest

lst = [1,2,4,6,3,8]
print(solution(lst))
