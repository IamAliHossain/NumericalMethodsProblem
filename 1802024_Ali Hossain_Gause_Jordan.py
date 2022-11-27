# x + y + z = 9
# 6x -y + z = 13
# 10x + y -z = 19
def gausseJordan() : 
    import numpy
    n = int(input("Enter The Number of varibale: "))
    #print(n)
    A = numpy.zeros((n,n+1))
    X = numpy.zeros(n)
    print("Enter the coefficients of matrix : ")
    for i in range(n):
        for j in range(n+1):
            A[i][j] = float(input('A[' + str(i) + '][' + str(j) + ']' + ' = ') )
    # print("The augumented matrix is : ")
    print(A)
    for i in range(n):
        if A[0][0] == 0.0 :
            print("No solution available Cause Divide by Zero detected.")
            break
        for j in range(n) :
            if i != j :
                ratio = A[j][i] / A[i][i]
                for k in range(n+1) :
                    A[j][k] = A[j][k] - ratio*A[i][k]

    print("The diagonal matrix is : ")
    print(A)
    print("The value of variables are :")
    for i in range(n):
        X[i] = A[i][n] / A[i][i]
    for i in range(n) :
        print('X%d =%0.2f' %(i, X[i]), end='\n')

    # print(X)
gausseJordan()