'''
    Original Problem Link: https://binarysearch.com/problems/Interleaved-Linked-List
'''

'''
    Given two linkedlists l0 and l1, return the two linkedlists interleaved,
    starting with l0
    At the end, just append the remaining elements of the list at the end

    Example
    l0 = 1 -> 3 -> 4
    l1 = 2 -> 5 -> 100

    Output l2 > 1 -> 2 -> 3 -> 5 -> 4 -> 100
'''

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def interleave(l0, l1):
    return None

#    So that is merging lls but without needing to check values. Let's make it harder

'''
    Given two sorted linkedlists l0 and l1, and array flips, merge the lists.
    
    l0 and l1 are sorted in increasing order, ie 0 -> 1 -> 2
    
    flips is an array of ints, each of which represents a count at which 
    the order of merging is flipped. the count matches the total number of nodes
    that have been added to the merged list

    Example0
    l0 = 1 -> 3 -> 4
    l1 = 2 -> 5 -> 100
    flips = [1, 3, 5]

    Output l2 > 1 -> 3 -> 4 -> 2 -> 5 -> 100
    Explanation - Initially, we add Node(1) to l2, since it is smaller
    Now that l2 has a count of 1 Node in its length, we hit the first flip
    This means we flip the direction, and now append the larger of the two elements
    so we add 3, and then 4 to l2
    At this point we can either add all of l1 by default condition.
    This is a meh example so I'll provide another after this. 
    
    Example1
    l0 = 1 -> 4 -> 19
    l1 = 2 -> 3 -> 25
    flips = [1, 2]

    Output l2 = 1 -> 4 ->  2 -> 3 -> 19 -> 25
    Explanation - Again we start with 1, no surprises there.
    the flip as count 1 means we grab the largest elements, and append 4 over 3
    flip again at count 2, and we're back to ascending order to add 3, and 19
    finally we hit our exit condition where l0 is empty, and just append the remainder of l1

    Hopefully this makes sense! I don't know if there's a lc/bs problem that matches up with this
    so that explanation will have to do. Try coming up with a short example of your own!
'''

def flippyMerge(l0, l1, flips):
    return None