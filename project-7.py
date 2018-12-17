
import sympy


def diff_or_min_or_max(z1):
    """This function determines whether a function is a minimum (maximum)"""

    mi = z1.find('min')
    ma = z1.find('max')
    if mi != -1:
        return 1
    if ma != -1:
        return 2
    else:
        return 0


def type_diff_f(derivative_x, derivative_y):
    """This function defines type of differentiable function"""

    derivative_x = str(derivative_x)
    derivative_y = str(derivative_y)

    a1 = derivative_x.find('x')
    a2 = derivative_x.find('y')
    b1 = derivative_y.find('x')
    b2 = derivative_y.find('y')

    if a1 == -1 and a2 == -1 and b1 == -1 and b2 == -1:
        return(0)
    if (a1 != -1 or b1 != -1) and (a2 != -1 or b2 != -1):
        return(1)
    if (a1 == -1 and b1 == -1) or (a2 == -1 and b2 == -1):
        return(2)


def derivat(z, v):
    """This function considers the derivative"""

    derivative = sympy.diff(z, v)
    return(derivative)


def expression_for_classic_function(derivative_x, derivative_y, Px, Py):
    """This function expresses x through y"""

    sympy.expr = (derivative_x - (Px/Py)*derivative_y)
    e_v = sympy.solve(sympy.expr, x)
    ratio = e_v.pop()
    ratio = (ratio/y)

    return(ratio)


def budget_for_classic_funcnion(I, ratio, Px, Py, y):
    """This function calculates the budget"""

    sympy.expr = y - I/(Py + ratio*Px)
    y = sympy.solve(sympy.expr, y)
    y = y.pop()

    return(y)


def variable_of_quasilinear_function(derivative_x, derivative_y):
    """This function defines quasilinear function variable"""

    derivative_x = str(derivative_x)
    derivative_y = str(derivative_y)

    a1 = derivative_x.find('x')
    a2 = derivative_x.find('y')
    b1 = derivative_y.find('x')
    b2 = derivative_y.find('y')

    if a1 == -1 and b1 == -1:
        return(1)
    if a2 == -1 and b2 == -1:
        return(0)


def expression_for_quasilinear_function(derivative_x, derivative_y, Px, Py, v):
    """This function expresses a variable in a quasilinear function"""

    sympy.expr = (derivative_x/derivative_y) - (Px/Py)
    e_v = sympy.solve(sympy.expr, v)
    ratio = e_v.pop()
    return(ratio)


def budget_for_quasilinear_function(v, e_v, I, Px, Py):
    """This function calculates the budget of quasilinear function"""

    if v == 0:
        q = I - (e_v * Px)
        if q <= 0:
            y = 0
            x = I / Px
        else:
            x = e_v
            y = I - e_v * Px
    if v == 1:
        q = I - (e_v * Py)
        if q <= 0:
            x = 0
            y = I / Py
        else:
            y = e_v
            x = I - e_v * Py
    return(x, y)


def parsing_of_string(z1):
    """This function divides the mathematical expression into two parts"""

    zf = z1.find('(')
    z1 = z1[(zf + 1):(-1)]
    zf2 = z1.find(')')
    z1 = z1[0:zf2]
    v_list = list(z1.split(','))
    l_p = v_list[0]
    l_p = eval(l_p)
    r_p = v_list[1]
    r_p = eval(r_p)
    return(l_p, r_p)


x = sympy.Symbol('x')
y = sympy.Symbol('y')

Px = float(input('Введите цену фактора x (в ден. ед./шт.):'))
Py = float(input('Введите цену фактора y (в ден. ед./шт.):'))
I = float(input('Введите предполагаемые затраты на факторы производства (в ден. ед.):'))
z1 = (input('Введите производственную функцию от x,y (в ед. продукта):'))

di = diff_or_min_or_max(z1)

if di == 0:

    z = eval(z1)
    derivative_x = derivat(z, x)
    derivative_y = derivat(z, y)

    t = type_diff_f(derivative_x, derivative_y)

    if t == 0:

        if (derivative_x/derivative_y) > (Px/Py):
            y = 0
            x = I/Px
            x = round(x, 3)
            y = round(y, 3)

        if (derivative_x/derivative_y) < (Px/Py):
            x = 0
            y = I/Py
            x = round(x, 3)
            y = round(y, 3)

        if (derivative_x/derivative_y) == (Px/Py):
            xq = I/Px
            xq = round(xq, 3)
            xq = str(xq)
            yq = I/Py
            yq = round(yq, 3)
            yq = str(yq)
            x = '     ' + xq
            y = 'либо ' + yq
    if t == 1:

        e_v = expression_for_classic_function(derivative_x, derivative_y, Px, Py)
        y = budget_for_classic_funcnion(I, e_v, Px, Py, y)
        y = str(y)
        y = eval(y)

        sympy.expr = x - e_v*y
        x = sympy.solve(sympy.expr, x)
        x = x.pop()
        x = str(x)
        x = eval(x)

        print(x)
        print(y)
        x = round(x, 3)
        y = round(y, 3)

    if t == 2:

        v = variable_of_quasilinear_function(derivative_x, derivative_y)
        if v == 0:
            e_v = expression_for_quasilinear_function(derivative_x, derivative_y, Px, Py, x)
        if v == 1:
            e_v = expression_for_quasilinear_function(derivative_x, derivative_y, Px, Py, y)
        list_answ = budget_for_quasilinear_function(v, e_v, I, Px, Py)
        x = list_answ[0]
        y = list_answ[1]
        x = round(x, 3)
        y = round(y, 3)

if di == 1:

    list_parts = parsing_of_string(z1)
    l_p = list_parts[0]
    r_p = list_parts[1]
    sympy.expr = (l_p - r_p)
    e_v = sympy.solve(sympy.expr, x)
    ratio = e_v.pop()
    ratio = ratio/y
    y = budget_for_classic_funcnion(I, ratio, Px, Py, y)
    x = y*ratio
    x = round(x, 3)
    y = round(y, 3)

if di == 2:
    a = parsing_of_string(z1)
    l_p = a[0]
    l_p_1 = str(l_p)
    r_p = a[1]
    r_p_1 = str(r_p)

    if l_p_1[-1] == 'x':
        ratio_x = ((l_p)/x)/Px
        ratio_y = ((r_p)/y)/Py
    else:
        ratio_x = ((r_p)/x)/Px
        ratio_y = ((l_p)/y)/Py

    if ratio_x > ratio_y:
        y = round(0, 3)
        x = round(I/Px, 3)
    if ratio_x < ratio_y:
        x = round(0, 3)
        y = round(I/Py, 3)
    if ratio_x == ratio_y:
        qx = str(round(I/Px, 3))
        qy = str(round(I/Py, 3))
        x = '     ' + qx
        y = 'либо ' + qy

print('')
print(x, 'ед. фактора x')
print(y, 'ед. фактора y')

z2 = eval(z1)
print('')
print('Q = ', z2)

print('')
input('Press ENTER to exit')
