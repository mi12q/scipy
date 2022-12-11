import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

sp.init_printing()
x = sp.symbols('x')
y = sp.Function('y')(x)
dydx = y.diff(x)
expr = sp.Eq(dydx, -2*y)
res = sp.dsolve(expr, ics = {y.subs(x,0): math.sqrt(2)})
print("Sympy solution:", res)


def ret_dfdt(f,t):
    dfdt = -2*f
    return dfdt


f0 = math.sqrt(2)
t = np.linspace(0,10)
f = odeint(ret_dfdt, f0, t)
plt.plot(t,f)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scipy solution")
plt.savefig("scipy.png")
plt.show()

y_val = []
for i in t:
    y_val.append(1.4142135623731*math.exp(-2*i))
sol_diff = []
for i in range(len(y_val)):
    sol_diff.append(abs(y_val[i]-f[i]))

plt.plot(t,y_val)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("SymPy solution")
plt.savefig("sympy.png")
plt.show()

plt.plot(t,sol_diff)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Difference between SciPy and SymPy solution")
plt.savefig("difference.png")
plt.show()
