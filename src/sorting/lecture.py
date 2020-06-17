
'''
Example - Basic Recursion
'''

def countdown_to_one(n):
    #2 base case (note, the base case is not always first)
    if n == 0:
        return
    print(n)
    countdown_to_one(n-1) # n - 1 is moving towards the base case.

countdown_to_one(5)



