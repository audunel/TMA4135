from __future__ import division

def secant_method(x0, x1, f, epsilon=0.001, n=50):
    """
    Computes the root of a function f given two starting points x_0 and x_1. The function terminates when the function is within epsilon of zero (default epsilon = 0.001) or exceeds n iterations (default n = 50)
    """
    for i in range(n):
        if abs(f(x1) - f(x0)) < epsilon:
            return x1
        x_temp = x1
        x1 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x_temp
    print('Maximum number of iterations exceeded! Terminated at solution x = ', x1)
