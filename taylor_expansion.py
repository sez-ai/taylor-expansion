""" taylor_expansion.py
Taylor Series Approximation for given function using sympy notation.

"""

import matplotlib.pyplot as plt
import numpy as np
from sympy.functions import sin,cos,exp
import sympy as sy
plt.rcParams["figure.figsize"] = (12,8) # w, h

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
def plot(function, x_upper_bound=None, appr_order=None, no_approx=False):
    """
    function: simpy function to be passed
    appr_order: degree of approximation polynom
    x_upper_bound: Boundaries of x during the visualization 
    no_approx: Only plot the original function, mutually exclusive with above arguments
    """
    x = sy.Symbol('x')
    if not no_approx:
        # approximation function,
        appr_function = taylor(function, 0, appr_order)
        x1 = np.linspace(-1 * x_upper_bound, x_upper_bound)
        y1 = []
        for k in x1:
            y1.append(appr_function.subs(x,k))
        plt.plot(x1,y1, label="approximation value")
        plt.suptitle('Taylor Series Expansion for '+ str(function) +' \n order: ' + str(appr_order))

    x_2 = np.linspace(-1*x_upper_bound,x_upper_bound)
    y_2 = []
    for k in x_2:
        y_2.append(function.subs(x,k))

    plt.plot(x_2, y_2, label="real value")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    return plt.show()

def demo():
    x = sy.Symbol('x')
    plot(appr_order=3, x_upper_bound=4, function=sin(x))
    plot(appr_order=3, x_upper_bound=4, function=exp(x))
    plot(appr_order=5, x_upper_bound=4, function=x**2+x**3-3)
    plot(appr_order=7, x_upper_bound=10, function=sin(x))
    

if __name__ == '__main__':
    demo()
