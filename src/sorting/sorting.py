# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) #Combined
    merged_arr = [0] * elements

    # Your code here
    #init the combined list that will hold the sorted elements from both a/b
    combined = []
    #these are our pointers, init the 2 pointers that start at each list 
    #start of element 
    a = 0
    b = 0 
    
    #Traverse 
    while a < len(arrA) and b < len(arrB):
        #compare the elements that a/b point at 
        if arrA[a] < arrB[b]:
            combined.append(arrA[a])
            #increment pointers 
            a += 1 
        else:
            combined.append(arrB[b])
            #increment pointers or else hang forever 
            b += 1

        # at this point, we've finished traversing one of the list completley 
        # the loop will stop when one of them fails, we dont know which one 
        # we need to add all of the elements from the other list to the combined list 
    while a < len(arrA): # we dont know which one so we check both
            combined.append(arrA[a])
            #increment pointers 
            a += 1 
    while b < len(arrB):
            combined.append(arrB[b])
            #increment pointers or else hang forever 
            b += 1


            


    return combined

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    #break the array down recurssively 

    #base case: when the list gets down to len of 1
    if len(arr) > 1:
        #each of these will recieve a list thats half the size
        #it will keep doing this until we break the condition, until they get to 1
        #getting the left half of the array with floor
        left = merge_sort(arr[:len(arr) // 2])  #recurse with our merge sort call which is going to return the left or the right 
        #getting the right side with len array divide by 2 until the end 
        right = merge_sort(arr[len(arr) // 2:]) #we'll pass it the split arrays 

        arr = merge(left, right)

    #merge them back up



    return arr








# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

