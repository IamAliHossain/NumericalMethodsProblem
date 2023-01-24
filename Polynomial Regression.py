from numpy import array, zeros, linalg

X = [0, 1, 2, 3, 4, 5]
Y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

X = array(X, float)
Y = array(Y, float)

N = len(X)
n = 2
A = zeros((n + 1, n + 1))
B = zeros(n + 1)
ans = zeros(n + 1)

A[0, 0] = N
for row in range(n + 1):

    for col in range(n + 1):
        if row == 0 and col == 0: continue

        A[row, col] = sum(X ** (row + col))

    B[row] = sum(X ** row * Y)

ans = linalg.solve(A, B)

print("The polynomial equation : ")
print('Y = %f' % ans[0], end=' ')
for i in range(1, n + 1):
    print('%+f X^%d' % (ans[i], i), end=' ')
print()