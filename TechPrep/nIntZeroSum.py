# Given an integer N, build a list of N distinct integers that sum to 0.
def findNumbers(N):
    sumList = []
     
    for i in range(1, N // 2 + 1):
         
        # Print 2 symmetric numbers
        sumList.append(i)
        sumList.append(-i)
         
    # add an extra 0 if N is odd
    if N % 2 == 1:
        sumList.append(0)