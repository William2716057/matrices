import numpy as np 
values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#row matrix 
rows = np.array(values)
print("Row matrix")
print(rows)
#column matrix
columns = np.array(values).reshape(-1,1 )
print("column matrix")
print(columns)
#square matrix 
numRows = 4
numCols = 4

squareMatrix = np.array(values).reshape(numRows, numCols)
print(squareMatrix)

#diagonal matrix 
#a type of matrix where all values will be arranged diagonally and remaning spaces will be filled with zero 

#create diagonal matrix with zeros 
n = len(values)
diagonalMatrix = np.zeros((n, n), dtype=int)

#enters values 
np.fill_diagonal(diagonalMatrix, values)

print("Diagonal matrix ")
print(diagonalMatrix)

