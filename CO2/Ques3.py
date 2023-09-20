#find smallest k values
import numpy as np
arr = np.array([10,48,34,29,71,56,12,23,1,67])
print("Array:",arr)
arr1 = np.sort(arr)
print("Sorted array:",arr1)
k= int(input("Enter the value of k: "))
print("First",k,"smallest value of the array:",arr1[:k])