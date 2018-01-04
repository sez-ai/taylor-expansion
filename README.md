
# Taylor Series Expansion



This _**toy project**_ plots [Taylor Approximation](https://en.wikipedia.org/wiki/Taylor_series) for given function and the original function.  
Dependences are listed in [requirements file](https://github.com/kirbiyik/taylor-expansion/blob/master/requirements.txt). 
Code was written for Python3 but should be fine with Python2, as well. 


To see the demo, enter command below. 
``` python 
python taylor_expansion.py 
```
Or you might want to enter the function manually, add special functions from [sympy functions](http://docs.sympy.org/latest/modules/functions/index.html). Open python interpreter in terminal. 
Don't forget to import.
``` python
import taylor_expansion as te
```

``` python
from sympy.functions import sin
``` 
``` python 
import sympy as sy
```
``` python 
x = sy.Symbol('x')
```
To plot _sinx_ function enter below
``` python 
te.lot(appr_order=8, x_upper_bound=20, function=sin(x))
```  
To plot x^2 + x^3 - 3
``` python 
te.plot(appr_order=0, x_upper_bound=4, function=x**2+x**3-3)

``` 
--- 
TODOs:

~~Add better types of invokation as soon as I have time to discover...~~


___
[Inspired by](http://firsttimeprogrammer.blogspot.com.tr/2015/03/taylor-series-with-python-and-sympy.html)
