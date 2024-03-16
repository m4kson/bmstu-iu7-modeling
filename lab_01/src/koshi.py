import math

eps = 10**-4

def razlozhenie(x):
    return 2 * x + -0.4 * x**2 / 2 + -1.4 * x**3 / 6 + 0.08 * x**4 / 24 + 0.28 * x**5 / 120

def f_1(v, u, x):
    return -0.1 * v**2 - (1 + 0.1 * x) * u

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

def picar_approx_3_1(u):
    return u**3 / 3

def picar_approx_3_2(u):
    return picar_approx_3_1(u) + u**7 / 63

def picar_approx_3_3(u):
    return picar_approx_3_2(u) + 2 * u**11 / 2079 + u**15 / 59535

def picar_approx_3_4(u):
    return picar_approx_3_3(u) + (2 / 93555)*u**15 + (2 / 3393495)*u**19 + \
        (2 / 2488563)*u**19 + (2 / 86266215)*u**23 + (1 / 99411543)*u**23 + \
        (2 / 3341878155)*u**27 + (1 / 109876902975)*u**31

def format(number):
    if type(number) == float:
        if number > 1000000:
            return '{:.4e}'.format(number)
        return '{:.4f}'.format(number)

    elif type(number) == int:
        return str(number)
    else:
        return number


def euler_method(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

    return y_values

def euler_method_for_system(f, x0, y0, v0, h, n):
    x_values = [x0]
    u_values = [y0]
    v_values = [v0]

    for i in range(n):
        x_new = x_values[-1] + h
        u_new = u_values[-1] + h * v_values[-1]
        v_new = v_values[-1] + h * f(v_values[-1], u_values[-1], x_values[-1])
        x_values.append(x_new)
        u_values.append(u_new)
        v_values.append(v_new)
    return u_values

def find_xmax(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]
    x_values_with_half_step = [x0]
    y_values_with_half_step = [y0]

    while True:
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

        for _ in range(2):
            x_new_with_half_step = x_values_with_half_step[-1] + h / 2
            y_new_with_half_step = y_values_with_half_step[-1] + h / 2 * f(x_values_with_half_step[-1], y_values_with_half_step[-1])
            x_values_with_half_step.append(x_new_with_half_step)
            y_values_with_half_step.append(y_new_with_half_step)

        if abs((y_new - y_new_with_half_step)) > eps:
            print("values: {}, {}".format(y_new, y_new_with_half_step))
            return x_values_with_half_step[-2]

def find_xmax_2(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]

    while True:
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        try:
            if abs((y_new - y_values[-1]) / y_values[-1]) < eps:
                return x_values[-1]
        except:
            x_values.append(x_new)
            y_values.append(y_new)
        x_values.append(x_new)
        y_values.append(y_new)

def task1():
    x_start = 0.5
    u_start = 1
    v_start = 2
    x_end = 1
    h = 1e-6

    n = math.ceil(abs(x_end - x_start) / h) + 1
    output_step = int(n / 10)

    euler_ans = euler_method_for_system(f_1, x_start, u_start, v_start, h, n)

    print(
        "-----------------------------------------------------------------------------------------------------------")
    print(
        "|                                           Задание №1: таблица                                           |")
    print(
        "-----------------------------------------------------------------------------------------------------------")
    print(
        "|         |                                          Метод                                                |")
    print(
        "|         |------------------------------------------------------------------------------------------------")
    print(
        "|         |               |               |                          Метод Пикара                         |")
    print(
        "|         |               |               |---------------------------------------------------------------|")
    print(
        "|    x    |  Разложение   |     Эйлера    |               |               |               |               |")
    print(
        "|         |               |               |   1-е прибл.  |   2-е прибл.  |   3-е прибл.  |   4-е прибл.  |")
    print(
        "-----------------------------------------------------------------------------------------------------------")

    for i in range(0, n, output_step):
        print("|{:^9.2f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|".format(x_start,
                                                                                    razlozhenie(x_start),
                                                                                    euler_ans[i],
                                                                                    picar_approx_1_1(x_start),
                                                                                    picar_approx_1_2(x_start),
                                                                                    picar_approx_1_3(x_start),
                                                                                    picar_approx_1_4(x_start)))

        print(
            "-------------------------------------------------------------------------------------------")
        x_start += h * output_step


def task2():
    x_start = 0.5
    x_end = 1
    h = 1e-6

    n = math.ceil(abs(x_end - x_start) / h) + 1
    output_step = int(n / 10)

    print(
        "-------------------------------------------------------------------------------------------")
    print(
        "|                                Задание №2: таблица                                      |")
    print(
        "-------------------------------------------------------------------------------------------")
    print(
        "|         |                                     Метод                                     |")
    print(
        "|         |--------------------------------------------------------------------------------")
    print(
        "|         |               |                          Метод Пикара                         |")
    print(
        "|         |               |---------------------------------------------------------------|")
    print(
        "|    x    |     Аналит    |               |               |               |               |")
    print(
        "|         |               |   1-е прибл.  |   2-е прибл.  |   3-е прибл.  |   4-е прибл.  |")
    print(
        "-------------------------------------------------------------------------------------------")

    for i in range(0, n, output_step):
        print("|{:^9.2f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|".format(x_start,
                                                                                    analytical_solution_2(x_start),
                                                                                    picar_approx_2_1(x_start),
                                                                                    picar_approx_2_2(x_start),
                                                                                    picar_approx_2_3(x_start),
                                                                                    picar_approx_2_4(x_start)))

        print(
            "-------------------------------------------------------------------------------------------")
        x_start += h * output_step


def task3():
    x_start = 0
    y_start = 0
    h = 1e-6
    x_end = find_xmax_2(f_3, x_start, y_start, h)
    #x_end = 1

    n = math.ceil(abs(x_end - x_start) / h) + 1
    output_step = int(n / 10)

    euler_ans = euler_method(f_3, x_start, y_start, h, n)

    print(
        "-------------------------------------------------------------------------------------------")
    print(
        "|                                           Задание №3: таблица                           |")
    print(
        "-------------------------------------------------------------------------------------------")
    print(
        "|         |                                          Метод                                |")
    print(
        "|         |--------------------------------------------------------------------------------")
    print(
        "|         |               |                          Метод Пикара                         |")
    print(
        "|         |               |---------------------------------------------------------------|")
    print(
        "|    x    |    Эйлера     |               |               |               |               |")
    print(
        "|         |               |   1-е прибл.  |   2-е прибл.  |   3-е прибл.  |   4-е прибл.  |")
    print(
        "-------------------------------------------------------------------------------------------")

    for i in range(0, n, output_step):
        print("|{:^9.2f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|{:^15.5f}|".format(x_start,
                                                                                    euler_ans[i],
                                                                                    picar_approx_3_1(x_start),
                                                                                    picar_approx_3_2(x_start),
                                                                                    picar_approx_3_3(x_start),
                                                                                    picar_approx_3_4(x_start)))

        print(
            "-------------------------------------------------------------------------------------------")
        x_start += h * output_step

