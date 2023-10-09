from ast import Num
from socket import NI_NUMERICHOST
import numpy as np 
values = [1,2,3,4]

#row matrix 
rows = np.array(values)
print("Row matrix")
print(rows)
#column matrix
columns = np.array(values).reshape(-1,1 )
print("column matrix")
print(columns)
#square matrix 
numRows = 2
numCols = 2

squareMatrix = np.array(values).reshape(numRows, numCols)
print(squareMatrix)

