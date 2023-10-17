import numpy as np
A=[[1,2,3],[4,5,6]]
B=[[7,8,9],[10,11,12]]
B_transpose=np.transpose(B)
result=np.dot(A,B_transpose)
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nTranspose of matrix B:")
print(B_transpose)
print("\nResult of A*B_tanspose")
print(result)