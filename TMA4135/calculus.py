from __future__ import division
from numpy import tan, exp

def main():
    solution = secant(lambda x : exp(-x) - tan(x), 1, 0.7)
    print(solution)

def secant(f, x0, x1, epsilon=0.0001, n=50):
    """
    Computes the root of a function f given two starting points x_0 and x_1. The function terminates when the difference between f(x1) and f(x2) is within epsilon of zero (default epsilon = 0.0001) or exceeds n iterations (default n = 50)
    """
    for i in range(n):
        if abs(f(x1) - f(x0)) < epsilon:
            return x1
        x_temp = x1
        x1 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x_temp
    print 'Maximum number of iterations exceeded! Terminated at solution x = ' + str(x1)
    return x1

def simpson(f, a, b, m=25):
    '''
    Given a function f  and endpoints a and b, approximates the integral of f from a to b using 2m steps
    '''
    n = 2*m
    h = (b - a)/n
    s = f(a) + f(b)
    for i in xrange(1, n, 2):
        s += 4 * f(a + i*h)
    for i in xrange(2, n - 1, 2):
        s += 2 * f(a + i*h)

    return (h*s)/3
