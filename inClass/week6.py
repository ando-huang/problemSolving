'''
    racecar > true
    racercar > false
    aba > true
    abc > false
'''
s = "abc"

def reverse(s):
    sR = [] # O(n) for space and time
    for i in range(len(s)): # for(int i = 0; i < s.length(); i++){...}
        sR.append(s[len(s)-1-i]) 
    return "".join(sR)

def isPalindrome(s):
    sR = reverse(s) # 
    if s == sR: # Time - O(n)
        return True
    return False
# print(isPalindrome(s))

def isPalindrome2(s):
    i, j = 0, len(s) -1
    while i < j:
        if s[i] != s[j]: # racecar
            return False
        i += 1
        j -= 1
    return True

'''
    racecar > true
    racercar > true
    aba > true
    abc > false

    ababca > true
    adabca > false 
'''

def almostPalindrome(s):
    i, j = 0, len(s) -1
    while i < j:
        if s[i] != s[j]: # racecar
            return isPalindrome2(s[i:j]) or isPalindrome2(s[i+1:j+1])
        i += 1
        j -= 1
    return True
s = 'adabca'
# print(almostPalindrome(s))

'''
    aaabcd
    aaabbc
    aaccerr
    acacerr

    acacerri
'''
# suppose s \in {a..z}
def canPalindrome(s):
    # count the number of occurrences for each character
    # if the len(s) is odd, then we can have 1 odd count
    # else no chars can have odd counts
    return False

# Complexity results -> ???

'''
    nums = [4, 4, 1, 6, 6, 1, 1, 1]
    > [
        [4, 4],
        [1],
        [6, 6]
        [1, 1, 1]
    ]
'''
def packBoxes(nums):
    packed, currList = [], []
    i = 0
    while i < len(nums):
        curr = nums[i]
        currList = [curr]
        i += 1
        while i < len(nums) and nums[i] == curr:
            currList.append(curr)
            i += 1
        packed.append(currList)
    return packed

nums = [4, 4, 1, 6, 6, 1, 1, 1, 2]
print(packBoxes(nums))