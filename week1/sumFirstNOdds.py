'''
    Given an integer n
    what is the sum of the first n odd integers?

    Example
    n = 5

    the first n odd integers are [1, 3, 5, 7, 9]
    their sum is 25

    Output > 25

    --
    n = 3
    first 3 odd integers are [1, 3, 5]
    sum = 9

'''

def sumFirstNOdds(n):
    s = 0
    for i in range(n): # [0 - n)
        # [0, 1, 2, 3, 4]
        s = s + (2 * i + 1)
    return s

def sum2(n):
    return n * n

n = 5
print(sumFirstNOdds(n))
