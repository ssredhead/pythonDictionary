#Write a function that determines the minimum number of flips required to
#fix an array's values so that each, representing flips of a coin, are opposites

def minFlip(a):
    return min(
        sum(n == i % 2 for i, n in enumerate(a)),
        sum(n == (i + 1) % 2 for i, n in enumerate(a))
    )

minFlip([1, 1, 0, 1, 1])
#2 flips necessary. The first index 1 -> 0, the last index 1 -> 0
minFlip([0, 1, 0, 1, 0])
#0 already fine
minFlip([1, 1, 1, 1, 1])
#2 index 1 and index 3
minFlip([0, 0, 0, 0, 0])
#2 index 1 and index 3