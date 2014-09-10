#-*- coding: utf-8 -*-

import numpy as np
from polynomial import poly
import matplotlib.pyplot as plt

def lagrange(x_values, y_values):
    '''
    Given the arrays x and y specifying a dataset of points (x,y), returns the values of a Lagrange polynomial of the dataset
    '''
    n = len(x_values)

    p = poly()
    for i in xrange(n):
        l = poly(y_values[i])
        for j in xrange(n):
            if i == j:
                continue
            d = 1 / (x_values[i] - x_values[j])
            l *= (poly([-x_values[j], 1.0]) * d)
        p += l
    return p
