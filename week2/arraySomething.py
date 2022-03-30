'''
    Given an array nums of ints, return the ??? in the array

    Constraints
    n <= 1,000,000 where n is the length of nums

    Preferably O(klogn)

    Problem link?
    <find it and paste it here>
'''

def s(nums):
    d = {}
    for n in nums:
        if n in d:
            continue
        d[n] = n * 100
    return len(d)

# TODO determine what the problem is, make an O(klogn) implementation

def sBetter(nums):
    return -1

def test():
    nums = [2, 2, 2, 3, 4, 5, 5, 6, 6, 7, 9]
    print(f"Expected {7}, got {s(nums)}")

test()
