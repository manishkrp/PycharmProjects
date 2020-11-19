
X = [[1,4,6],
     [4,6,7],
     [5,6,4]]

Y = [[4,5,6],
     [5,7,9],
     [6,7,5]]

Z = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
          for k in range(len(Y)):
               Z[i][j] + = X[i][k] * Y[j][k]


print(Z[i][j])
