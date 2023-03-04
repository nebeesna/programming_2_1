from math import pi, cos, sqrt, sin, tan, exp
import matplotlib.pyplot as plt
import random
from sympy import *
from sympy.calculus.util import *


x, y = symbols('x y')

f = sympify(input("Enter function f(x): "))
g = sympify(input("Enter function g(x): "))
ab = input("Enter segment [a, b]: ").split()
a = float(sympify(ab[0]))
b = float(sympify(ab[1]))
x_l = []
f_l = []
g_l = []

u = a

while u <= b:
    x_l.append(u)
    f_l.append(f.subs(x, u))
    g_l.append(g.subs(x, u))
    u += 0.1

c = min(min(f_l), min(g_l))
d = max(max(f_l), max(g_l))

dot_x = []
dot_y = []
for i in range(2500):
    dot_x.append(random.uniform(a, b))
    dot_y.append(random.uniform(c, d))

ins_x = []
ins_y = []
out_x = []
out_y = []
for i in range(2500):
    x_ = dot_x[i]
    if dot_y[i] < max(f.subs(x, x_), g.subs(x, x_)) and dot_y[i] > min(f.subs(x, x_), g.subs(x, x_)):
        ins_x.append(dot_x[i])
        ins_y.append(dot_y[i])
    else:
        out_x.append(dot_x[i])
        out_y.append(dot_y[i])

s = (len(ins_x)/2500)*(b - a)*(d - c)

plt.scatter(out_x, out_y, color='#99e1d9')
plt.scatter(ins_x, ins_y, color='#a8a3cc')
plt.xlabel(f"S = {round(s, 4)}", fontsize=15)
plt.plot([a, a], [c, d], linestyle='--', color='grey')
plt.plot([b, b], [c, d], linestyle='--', color='grey')
plt.plot([a, b], [c, c], linestyle='--', color='grey')
plt.plot([a, b], [d, d], linestyle='--', color='grey')
plt.plot(x_l, f_l, color='#4a304a', linewidth=3, label=f"f(x) = {f}")
plt.plot(x_l, g_l, color='#043a4e', linewidth=3, label=f"g(x) = {g}")
plt.legend()
plt.grid(True)
plt.show()

