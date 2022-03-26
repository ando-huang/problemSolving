'''
    Problem Link
    https://binarysearch.com/problems/Equation-Typo

    :shrug 

    below is partial code, it handles extracting 
    int values for a, b, and c in O(n)

    feel free to use or not use the provided code

'''

def solve(self, s):
    a, b, c = 0, 0, 0
    curr = 0
    for char in s:
        if char == '+':
            a = curr
            curr = 0
        elif char == '=':
            b = curr
            curr = 0
        else:
            curr *= 10
            curr += int(char)
    c = curr

    # print(a, b, c)

    inserts = 0
    
    # TODO determine how many inserts we need

    return inserts
