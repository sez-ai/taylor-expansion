""" taylor_expansion.py
Taylor Series Approximation for given function using sympy notation.

"""

import matplotlib.pyplot as plt
import numpy as np
from sympy.functions import sin,cos,exp
import sympy as sy



def factorial(k):
    if k == 0:
        return 1
    acc = k
    while k >1 :
        k -= 1
        acc = acc * k
    return acc


def taylor(func, x_0, n):
    """
    func: function to be expanded
    x_0: about x_0
    n: order
    """
    x = sy.Symbol('x')
    p = 0;
    # n denotes upper index
    for i in range(n+1):
        p += (func.diff(x,i).subs(x,x_0)) * ((x-x_0)**i) / factorial(i)
    return p


# approximation of first 'n' terms
def plot(appr_order, x_upper_bound, function):
    x = sy.Symbol('x')
    # approximation function,
    appr_function = taylor(function, 0, appr_order)
    x1 = np.linspace(-1 * x_upper_bound, x_upper_bound)
    y1 = []
    for k in x1:
        y1.append(appr_function.subs(x,k))
    plt.plot(x1,y1, label="approximation value")

    x_2 = np.linspace(-1*x_upper_bound,x_upper_bound)
    y_2 = []
    for k in x_2:
        y_2.append(function.subs(x,k))
    plt.suptitle('Taylor Series Expansion for '+ str(function) +' \n order: ' + str(appr_order))
    plt.plot(x_2, y_2, label="real value")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    return plt.show()

def demo():
    x = sy.Symbol('x')
    plot(appr_order=1, x_upper_bound=3, function=sin(x))
    plot(appr_order=1, x_upper_bound=10, function=exp(x))
    plot(appr_order=3, x_upper_bound=4, function=sin(x))
    plot(appr_order=3, x_upper_bound=4, function=exp(x))
    plot(appr_order=7, x_upper_bound=10, function=sin(x))
    plot(appr_order=7, x_upper_bound=10, function=exp(x))
    plot(appr_order=15, x_upper_bound=10, function=sin(x))
    plot(appr_order=15, x_upper_bound=10, function=exp(x))


demo()
