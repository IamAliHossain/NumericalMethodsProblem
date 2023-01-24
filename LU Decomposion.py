import numpy 


def decomposition(A):
    N = len(A)
    L = numpy.zeros((N,N))    
    U = numpy.zeros((N,N))    

    for j in range(N):                                     
        
        U[j,j] = 1                                          

        for i in range(j):                                  
            if j == 0: break                               
            
            U[i,j] = (A[i,j] - sum(L[i,:i]*U[:i,j])) / L[i,i]

           
        for i in range(j, N):                                 

            L[i,j] = A[i,j] - sum(L[i,:j]*U[:j,j])              

    print('LU Decomposition:')
    print('[L] =\n', L, sep='')
    print('[U] =\n', U, sep='', end='\n\n')
    return L, U


def solveLU(A, B):
    L, U = decomposition(A)
    N = len(L)
    
    X = numpy.zeros(N)
    Y = numpy.zeros(N)

    
    for i in range(N):                                      
        Y[i] = (B[i] - sum(L[i,:i] * Y[:i])) / L[i,i]       

    for i in range(N-1, -1, -1):                           
        X[i] = (Y[i] - sum(U[i,i+1:] * X[i+1:]))           

    return X


A = numpy.array([[3,  -.1, -.2],
           [.1,  7,  -.3],
           [.3, -.2, 10]], float)
B = numpy.array([10.3, 33.6, 60.2], float)

N = len(A)

X = solveLU(A, B)

print("The Solution of the System:")
for i in range(N):
    print('X[', str(i+1), '] = ', round(X[i], 6), sep='')
    