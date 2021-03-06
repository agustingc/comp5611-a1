from a1 import *

'''
    Test square
'''
def test_square():
    a = array([[1, 2, 3], [1, 2, 3]])
    assert(not square(a))
    a = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    assert(square(a))


def test_gauss_multiple():
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    b = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    print('a:\n',a,'\n')
    print('b:\n', b,'\n')
    solution = gauss_multiple(a, b)  # result is now in b or solution
    print('sol:\n', solution)

    na = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    nb = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    from numpy.linalg import solve
    nsolution = solve(na, nb)
    print('linalg sol:\n',nsolution,'\n')


def test_gauss_multiple_pivot():
    a = array([[0, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    b = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    print('a:\n',a)
    print('b:\n', b)
    solution = gauss_multiple_pivot(a, b) # result is now in b or solution
    print('sol:\n', solution,'\n')

    na = array([[0, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    nb = array([[-14, 22], [36, -18], [6, 7]], dtype=float_)
    from numpy.linalg import solve
    nsolution = solve(na, nb)
    print('linalg sol:\n',nsolution)


def test_inverse():
    a = array([[6, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    inva = matrix_invert(a)
    print(inva)


def test_diagonal():
    '''
    a = array([[0, 4, 1], [-4, 6, -4], [1, -4, 6]], dtype=float_)
    print(a,'\n')
    print ('Length of main diagonal:\n', len(diagonal(a)))
    c= diagonal(a,-1)
    c = append(c,0)
    print(c,'\n')
    print ('Length of lower diagonal:\n', len(c))
'''

    print(tridiag_solver_n(5))


def test_fit_poly():
    my_data = [(0, 2), (1, 6), (2, 24), (3, 62)]
    #my_data = [(0, -1), (1, -2), (0, -1)]
    coeffs = fit_poly(my_data)
    print(coeffs)


'''
    Run code
'''
#test_square()
#test_gauss_multiple()
#test_gauss_multiple_pivot()
#test_inverse()
#test_diagonal()
test_fit_poly()

