import numpy as np

arr_zeros=np.zeros((2,3))
print("\nArray of zeros:\n", arr_zeros)

arr= np.array([[1,2,3],[5,4,6],[7,8,9]])
print(arr)

print("Element at [1,2] (2D indexing):", arr[1,2])

#slice rows from 0 to 1 and columns from 1 to 2
print("Slice row 0:2, cols 1:3\n", arr[0:2,1:3])

#Fancy Indexing
#use lists or arrays of indices to grab specific elements
indices=[0,2] #grab rows at indices 0 and 2
indices1=[2,0] #flipped
arr_2=arr[indices, :]

print("Fancy indexing (select rows [0,2]):\n", arr_2)

#Boolean indexing

bool_mask=arr>4 #return true for values that are greater than 4 and false those aren't

print(bool_mask)

print("elements >4:", arr[bool_mask]) # prints those elements

# combinig boolean and logical operators

bool_mask_combined


