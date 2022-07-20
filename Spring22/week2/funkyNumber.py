'''
    Given an integer n, return ???

    Example
    n = 153
    output - True

    Explanation ???

    [easy]Problem Link ???
'''

def s(n):
    t = n
    d = []
    while t > 0:
        d.append(t%10)
        t //= 10
    s = 0
    for i in d:
        s += i ** len(d)
    return s == n

# TODO Determine what the function does
# Try to find the binarysearch.com link, and update it in the header

# Can you come up with a more efficient solution?

def sBetter(n):
    return False

def test():
    n = 153
    print(f"Expected {True}, got {s(n)}")
    n = 370
    print(f"Expected {True}, got {s(n)}")
    n = 371
    print(f"Expected {True}, got {s(n)}")
    n = 422
    print(f"Expected {False}, got {s(n)}")

test()
