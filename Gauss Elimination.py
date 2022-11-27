
#Solve this equation

# 3x1 -2x2 + 5x3 = 2
# 4x1 + 5x2 + 8x3 + x4 = 4
# x1 + x2 + 2x3 + x4 = 5
# 2x1 + 7x2 + 6x3 + 5x4 = 7
# The solution of the system:
# [ 28.77777778   2.16666667 -16.           6.05555556]

import numpy as np
# from numpy import array, zeros
a = np.array([  [3, -2, 5, 0],
                [4, 5, 8, 1],
                [1, 1, 2, 1],
                [2, 7, 6, 5]], float)

b = np.array([2, 4, 5, 7], float)
n = len(b)
x = np.zeros(n, float)
#Elimination part

for i in range (n-1) :
    for j in range (i+1, n) :
        if a[j][i] == 0 : continue
        ratio = a[i][i] / a[j][i]
        for k in range (i, n) :
            a[j][k] = a[i][k] - ratio * a[j][k]
        b[j] = b[i] - ratio * b[j]
print(a)
print(b)

#Back substitution
for i in range (n-1, -1, -1) :
    sum_ax = 0 
    for j in range(i+1, n) :
        sum_ax += a[i][j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i][i]
print("The solution of the system: ")
print(x)


































# for i in range (n-1) : 
#     for j in range (i+1, 2) :
#         if a[j, i] == 0 :
#             continue
#         ratio = a[i][i] / a[j][i]
#         for k in range (i, n) :
#             a[j][k] = a[i][k] - ratio * a[j][k]
#         b[j] = b[i] - b[j] * ratio 
# print(a)
# print(b)
