#calculate the euclidean distance using numpy
import numpy as np
p1 = np.array([1,2,3])
p2 = np.array([1,1,1])
distance = np.linalg.norm(p1-p2)
print("Distance = ",distance)
