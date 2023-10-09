import numpy as np 
values = [1,2,3,4,5,]

#row matrix 
rows = np.array(values)
print("Row matrix")
print(rows)
#column matrix
columns = np.array(values).reshape(-1,1 )
print("column matrix")
print(columns)
