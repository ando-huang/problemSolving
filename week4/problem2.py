'''
    Problem Link: https://binarysearch.com/problems/Linked-List-Delete-Last-Occurrence-of-Value
'''

'''
    Given a singly linked list populated with ints and a target value k
    remove the last occurrence of k in the linkedlist.
    If k is not in the list, do nothing and return the original list
'''

class LLNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def removeLastK(head, k):
    return None

'''
    Bonus round :D
    
    Given a linkedlist of ints, target value k
    find and return all values that have k or more occurrences
    
    What would be a good way to return these values?
    How much additional storage do we need?

    Suppose the LL contained single chars from the set of lowercase letters a-z
    how does that affect the amount of storage we need? 
'''

def kOrMoreOccurrences(head, k):
    return None

