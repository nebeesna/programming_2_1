from sympy import diff, simplify, sympify, symbols
from math import sin, cos, tan, sqrt, exp
import matplotlib.pyplot as plt

# Нехай в декартових координатах параметрично задано деяку криву
# L: x=x(t), y=y(t), 0<t<T.
# Нехай задано деяку періодичну функцію g(s) з достатньо малою амплітудою.
# Написати програму, яка на основі заданих з клавіатури функцій
# малює криву, яка утворюється з графіка функції g(s) в
# декартових координатах шляхом трансформації площини,
# при якій вісь s переходить в криву L. Для прикладу, якщо крива L – коло,
# а функція g(s) має вигляд g(s)=A sin(ks), то можливий варіант
# графіка отриманої кривої є таким, як на рисунку:
t, s = symbols('t s')

x = sympify(input("Enter function x(t): "))
y = sympify(input("Enter function y(t): "))
g = sympify(input("Enter function g(s): "))
step = float(input("Enter step: "))
tab = input("Enter segment [a, b]: ").split()
t_a = float(sympify(tab[0]))
t_b = float(sympify(tab[1]))

x_d = diff(simplify(x))
y_d = diff(simplify(y))

x_l = []
y_l = []
x_g = []
y_g = []
st = 0

while t_a <= t_b:
    st = st + step * sqrt(x_d.subs(t, t_a) ** 2 + y_d.subs(t, t_a) ** 2)
    x_l.append(x.subs(t, t_a))
    y_l.append(y.subs(t, t_a))
    x_g.append(x.subs(t, t_a) + (g.subs(s, st) / (sqrt(x_d.subs(t, t_a)**2 + y_d.subs(t, t_a)**2)) * y_d.subs(t, t_a)))
    y_g.append(y.subs(t, t_a) + (g.subs(s, st) / (sqrt(x_d.subs(t, t_a)**2 + y_d.subs(t, t_a)**2)) * -(x_d.subs(t, t_a))))

    t_a += step

plt.plot(x_l, y_l)
plt.plot(x_g, y_g)
plt.grid()
plt.gca().set_aspect("equal")
plt.show()


# Enter function x(t): t
# Enter function y(t): sin(t)
# Enter function g(s): 0.2*sin(10*s)
# Enter step: 0.001
# Enter segment [a, b]: -10 10
