'''
    Hello! This is an extension of the inclass Code from week 4
    The problem we solved in class was
    https://binarysearch.com/problems/Uber-Pool
    but the solution had very poor runtime.

    I discussed a potential solution with Kairui afterwards,
    the description is below. Try to implement it, make changes as necessary

    Good luck!
'''

'''
    We want to use maxPos from the current solution, so that can be brought over
    Using maxPos, create an array of ints, all 0s, of length maxPos
    this array will represent the net changes to people on the uber
    Thats one iteration of trips so far, O(n) at this point

    To populate the array, iterate through trips again. Suppose we have a trip
    [start=1, end=20, ppl=5]
    At the start position, we want to increment the array's value by ppl
    at the end position, decrement by those ppl because they got off

    once we populate the array, we can iterate through it. 
    If the number of available seats ever drops below 0, we cannot do this in one trip

    email/slack me with any questions! it might also help to try doing the problem in another language for fun 
'''

def solve(trips, capacity):
    return False