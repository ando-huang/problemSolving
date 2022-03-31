'''
    Given an array nums of ints, return the ??? in the array

    Constraints
    n <= 1,000,000 where n is the length of nums

    Preferably O(klogn)

    Problem link?
    <find it and paste it here>
'''

# numUniquesInArray(arr) takes in array and returns number
# of unique elements
def s(nums):
    d = {} # dict
    for n in nums:
        if n in d:
            continue
        d[n] = 0
    return len(d)

# TODO determine what the problem is, make an O(klogn) implementation

def sBetter(nums):
    return -1

def test():
    arr = [1, "hello", False]
    nums = [2, 2, 2, 3, 4, 5, 5, 6, 6, 7, 9]
    print(f"Expected {3}, got {s(arr)}")

test()
