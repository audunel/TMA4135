from __future__ import division
import numpy as np
from calculus import simpson

def fourierSeries(f, n):
    '''
    Given a 2pi-periodic function f, returns a list of fourier-coefficients, represented as tuples.
    '''
    coefficients = list()
    a = (2.0*np.pi)**(-1) * quad(f, -np.pi, np.pi)[0]
    coefficients.append(a)
    for i in xrange(1,n+1):
        a = np.pi**(-1) * simpson(lambda x : f(x)*np.cos(n*x), -np.pi, np.pi)
        b = np.pi**(-1) * simpson(lambda x : f(x)*np.sin(n*x), -np.pi, np.pi)
        coefficients.append((a, b))
    return coefficients
