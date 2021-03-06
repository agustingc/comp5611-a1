from numpy import *
#from numpy import shape

'''
   PART 1: Warm-up
'''


def example_func():
    '''
      Important: READ THIS CAREFULLY. 
      Task: This function is an example, you don't have to modify it.
      Example: Nothing to report here, really.
      Test: This function is is tested in tests/test_example.py
            This test just gives you a bonus, yay!
      Hint: The functions below have to be implemented in Python, without
            using any function from numpy's linear algebra module. In each function, a
            docstring formatted as the present one explains what the 
            function must do (Task), gives an example of output 
            (Example), explains how it will be evaluated (Test), and 
            may give you some hints (Hint).
    '''
    return 'It works!'


def square(a):
    '''
      Task: This function tests if a matrix is square. It returns True 
            if a represents a square matrix.
      Parameters: a is a numpy array.
      Example: square(array([[1, 2], [3, 4]])) must return True.
      Test: This function is is tested in tests/test_square.py
      Hint: Use numpy's shape function.
    '''

    ## YOUR CODE GOES HERE
    n,m = shape(a)  #save value of elements in tuple shape(a) in variables n, m
    return n == m

    raise Exception("Function not implemented")


'''
  Part 2: Resolution of linear systems for polynomial interpolation
'''


def fit_poly_2(points):
    '''
      Task: This function finds a polynomial P of degree 2 that passes 
            through the 3 points contained in list 'points'. It returns a numpy
            array containing the coefficient of a polynomial P: array([a0, a1, a2]),
            where P(x) = a0 + a1*x + a2*x**2. Every (x, y) in 'points' must 
            verify y = a0 + a1*x + a2*x**2.
      Parameters: points is a Python list of 3 pairs representing 2D points.
      Example: fit_poly_2([(0, -1), (1, -2), (2, -9)]) must return array([-1, 2, 3])
      Test: This function is is tested by the following functions in tests/test_fit_poly.py:
            - test_fit_poly_2 tests a basic fit
            - test_fit_poly_raises tests that the function raises an 
              AssertionError when the polynomial cannot be fit (for 
              instance, 3 points are aligned).
      Hint: This should be done by solving a linear system.
    '''

    ## YOUR CODE GOES HERE
    return fit_poly(points)
    raise Exception("Function not implemented")


def fit_poly(points):
    '''
      Task: This function is a generalization of the previous one. It 
            finds a polynomial P of degree n that passes 
            through the n+1 points contained in list 'points'. It 
            returns a numpy array containing the coefficient of a 
            polynomial P: array([a0, a1, ..., an]), where P(x) = a0 + 
            a1*x + a2*x**2 + ... + an*x**n. Every (x, y) in 'points' 
            must verify y = P(x).
      Parameters: points is a Python list of pairs representing 2D points.
      Examples: fit_poly([(0, -1), (1, -2), (2, -9)]) must return 
                array([-1, 2, -3]) (as in the previous function) fit_poly([(0, 2), 
                (1, 6), (2, 24), (3, 62)]) must return array([2, -1, 4, 1])
      Test: This function is is tested by the following functions in tests/test_fit_poly.py:
            - test_fit_poly tests a basic fit
            - test_fit_poly_n tests the fit on a random polynomial of degre <= 6.
      Hint: This should be done by solving a linear system.
    '''

    ## YOUR CODE GOES HERE
    #Get degree of polynomial
    n = len(points)
    print('n: ', n)
    m = n - 1
    #Populate x_data, y_data by unpacking point (array of tuples)
    x_data = zeros(n,dtype=float_)
    y_data = zeros(n, dtype=float_)
    for i in range(0,n):
        x_data[i], y_data[i] = points[i]
    print('x_data :' , x_data)
    print('\ny_data: ', y_data)
    ''' For convenience, s[i] will contain sum_i x_i^h, where h = 0, 2m, i = 0, 1, ..., n
        and b[i] will contain sum_i(x_i^k*y_i) where k = 0,1, ..., m and i = 0, 1, ..., n
    '''
    s = zeros(2*m+1, dtype=float_)
    b = zeros(m+1, dtype=float_)
    for i in range(2*m+1):
        s[i]=sum(x_data**i)
        if i<(m+1): #Populate b for the first m iterations
            b[i] = sum(y_data*x_data**i)
    print('\ns: ', s)
    # Populate the coefficient matrix A
    A = zeros((m+1,m+1), dtype=float_)
    for k in range (0,m+1):
        for j in range (0,m+1):
            A[k,j]=s[j+k]
    print('\nA: ', A)
    #Solve system of linear equations
    a = gauss_multiple_pivot(A,b)
    return a
    raise Exception("Function not implemented")


'''
  Part 3: Tridiagonal systems
'''

def tridiag_solver_n(n):
    '''
      Task: This function returns the solution of the following tridiagonal equations:
            4x[1] - x[2] = 9
            -x[i-1] + 4x[i] - x[i+1] = 5, i=2,....n-1
            -x[n-1] + 4x[n] = 5
            The system of equations is the same
            as in problem 2.2.9 in the Textbook, except that here n is a 
            parameter of the function. All correct answers will be accepted,
            but you are strongly encouraged to exploit the tridiagonal nature
            of the system.
      Parameters: n is an integer representing the dimension of the system.
      Examples: tridiag_solver_n(2) must return array([41/15, 29/15])
      Test: This function is is tested by the function in tests/test_tridiag_solver.py.
    '''

    ## YOUR CODE GOES HERE
    #Verify that matrix will be at least 3x3
    assert (n>2)
    a=zeros((n,n), dtype=float_)
    b = zeros(n, dtype=float_)
    #Populate matrices a and b
    for i in range (0,n):
        if i==0:
            a[i,0]=4
            a[i,1]=-1
            b[i] =9
        elif i==n-1:
            a[i,n-2]=-1
            a[i,n-1]=4
            b[i]=5
        else:
            a[i,i-1] = -1
            a[i,i] = 4
            a[i,i+1] = -1
            b[i] = 5
    #TEST
    #print('A:\n', a, '\n')
    #print('b:\n', b, '\n')
    #Convert to diagonal vectors
    c = diagonal(a,-1).copy()
    d = diagonal(a,0).copy()
    e = diagonal(a,1).copy()
    c = append(c,0)
    e = append(e,0)
    tridiag_decomp(c, d, e)
    return tridiag_solve(c, d, e, b)
    raise Exception("Function not implemented")

#Code from course notes
def tridiag_decomp(c, d, e):
    assert(len(c) == len(d) == len(e))
    n = len(c)
    for k in range(1, n):
        lambd = c[k-1]/d[k-1]
        d[k] -= lambd*e[k-1]
        c[k-1] = lambd

#Code from course notes slightly modified
def tridiag_solve(c, d, e, b): # watch out, input has to be in LU form!
    assert(len(c) == len(d) == len(e) == len(b))
    n = len(c)
    # forward substitution
    y = zeros(n, dtype=float_)
    y[0]=b[0]
    for i in range(1, n):
        y[i] = b[i]-c[i-1]*y[i-1] # Here we use y to store y
    # back substitution
    x = zeros(n, dtype=float_)
    x[n-1] = y[n-1]/d[n-1] # Here we use x to store x
    for i in range (n-2, -1, -1):
        x[i] = (y[i]-e[i]*x[i+1])/d[i]
    return x


'''
  Part 4: Gauss Elimination for more than 1 equation
'''

def gauss_multiple(a, b):
    '''
      Task: This function returns the solution of the system written as
            AX=B, where A is an n x n square matrix, and X and B are n x m matrices.
            It is equivalent to solving m systems of the form Ax=b, where
            x and b are column vectors. You have to extend the implementation
            of Gauss elimination presented in the course to work with m constant
            vectors instead of only 1. This is problem 2.1.14 in the textbook.
            It is up to you to decide if your function will modify a and b (the
            tests should work in both cases).
      Parameters: a is a numpy array representing a square matrix. b is a numpy
            array representing a matrix with as many lines as in a.
      Test: This function is is tested by the function test_gauss_multiple in tests/test_gauss_multiple.py.
      Hint: Start from the implementation shown in the course!
    '''

    ## YOUR CODE GOES HERE
    gauss_multiple_elimin(a,b,)
    return gauss_substitution(a,b)
    raise Exception("Function not implemented")


#for gauss_multiple
def gauss_multiple_elimin(a,b,verbose=False):
    n, m = shape(a)     #must be square
    n2, m2 = shape(b)   #does not need to be square
    assert(n==n2)
    for k in range (0,n-1):     #range(start,stop[,step])
        for i in range (k+1, n):
            assert(a[k,k]!=0) #verify what to do later
            if(a[i,k]!=0): #no need to do anything when lambda is 0
                lmbda = a[i,k]/a[k,k]
                a[i,k:n]=a[i,k:n] - lmbda * a[k,k:n] #apply operation to row i of A
                b[i,:]=b[i,:] - lmbda * b[k,:] #apply operation to row i of b
            if verbose:
                print('a:\n',a,'\nb:\n',b,'\n')


def gauss_substitution(a,b):
    n, m = shape(a)
    #Verify the n*n dimensions of B
    n2=1
    m2=1
    if len(shape(b))==1:
        n2, = shape(b)
    elif len(shape(b))==2:
        n2, m2 = shape(b)
    else:
        raise Exception("B has more than 2 dimensions")
    assert (n==n2)
    if m2>1:
        x = zeros([n,m2], dtype= float_)
        for i in range (n-1,-1,-1): #decreasing index, #range(start,stop[,step]) -> iterates over every row of solution matrix x
            for j in range(0,m2):
                x[i,j]=(b[i,j] - dot(a[i,i+1:],x[i+1:,j]) ) / a[i,i]
        #return n*m system of solutions
        return x
    else:
        x = zeros([n], dtype= float_)
        for i in range (n-1,-1,-1): #decreasing index, #range(start,stop[,step]) -> iterates over every row of solution matrix x
            x[i] = (b[i] - dot(a[i,i+1:],x[i + 1:]))/a[i, i]
        #return n*m system of solutions
        return x


def gauss_multiple_pivot(a, b):
    '''
      Task: This function returns the same result as the previous one,
            except that it uses scaled row pivoting.
      Parameters: a is a numpy array representing a square matrix. b is a numpy
            array representing a matrix with as many lines as in a.
      Test: This function is is tested by the function 
            test_gauss_multiple_pivot in tests/test_gauss_multiple.py.
    '''

    ## YOUR CODE GOES HERE
    gauss_elimin_pivot(a,b)
    ''' The determinant of a triangular matrix 
        is the product of the diagonal elements
    '''
    det = prod(diagonal(a))
    assert(det!=0)
    return gauss_substitution(a,b)
    raise Exception("Function not implemented")


#for gauss_multiple_pivot
def swap(a, i, j):
    if len(shape(a)) == 1:
        a[i],a[j] = a[j],a[i] # unpacking
    else:
        a[[i, j], :] = a[[j, i], :]

#for gauss_multiple_pivot
def gauss_elimin_pivot(a,b,verbose=False):
    #A
    n, m = shape(a)     #must be square
    #B
    n2=1
    m2=1
    if len(shape(b))==1:
        n2, = shape(b)   #does not need to be square
    elif len(shape(b))==2:
        n2, m2 = shape(b)   #does not need to be square
    else:
        raise Exception("B has more than 2 dimensions.")
    assert(n==n2)
    #Used for pivoting
    s = zeros(n, dtype =float_)
    for i in range (0,n):
        s[i] = max(abs(a[i, :])) #max of row i in A
    # Pivoting
    #print(a)
    for k in range (0,n-1):     #range(start,stop[,step])
        p = argmax(abs(a[k:, k]) / s[k:]) + k
        swap(a,p,k) #swap rows in matrix A
        swap(b,p,k) #swap rows in matrix b
        swap(s,p,k) #swap rows in vector  s
        #Apply row operations
        for i in range (k+1, n):
            assert(a[k,k]!=0) #verify what to do later
            if(a[i,k]!=0): #no need to do anything when lambda is 0
                lmbda = a[i,k]/a[k,k]
                a[i,k:n]=a[i,k:n] - lmbda * a[k,k:n] #apply operation to row i of A
                if m2==1:
                    b[i] = b[i] - lmbda * b[k]  # apply operation to row i of b
                else:
                    b[i,:]=b[i,:] - lmbda * b[k,:] #apply operation to row i of b
            if verbose:
                print('a:\n', a, '\nb:\n', b, '\n')


def matrix_invert(a):
    '''
      Task: This function returns the inverse of the square matrix a passed 
            as a paramter. 
      Parameters: a is a numpy array representing a non-singular square matrix.
      Test: This function is is tested by function test_inverse in tests/test_inverse.py
      Hint: Remember that the inverse of A is the solution of n linear systems of n 
            equations.
    '''
    ## YOUR CODE GOES HERE
    #Check if matrix is square
    assert(square(a))
    n, m = shape(a)
    i = identity(n,dtype=float_)
    return gauss_multiple_pivot(a,i)
    raise Exception("Function not implemented")
