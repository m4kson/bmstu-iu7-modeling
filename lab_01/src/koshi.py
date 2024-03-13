import math

def f_2(x, u):
    return u**3 + 2*u*x

def f_3(x, u):
    return x**2 + u**2

def analytical_solution_2(u):
    return math.exp(u**2) - (u**2 + 1) / 2

def picar_approx_2_1(u):
    return 0.5 + u**2 / 2 + u**4 / 4

def picar_approx_2_2(u):
    return picar_approx_2_1(u) + u**4 / 4 + u**6 / 12

def picar_approx_2_3(u):
    return picar_approx_2_2(u) + u**6 / 12 + u**8 / 48

def picar_approx_2_4(u):
    return picar_approx_2_3(u) + u**8 / 48 + u**10 / 240

def picar(x_max, h, approx_fun):
    result = []
    x, u = 0, 0
    while abs(x) < abs(x_max):
        result.append(u)
        x += h
        u = approx_fun(x)
        return result

