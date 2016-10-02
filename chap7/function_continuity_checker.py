'''
Check the continuity of a given function with a single variable.
'''

from sympy import Limit, Symbol, sympify

def calc_left_limit(f, var, var0):
    left_limit = Limit(f, var, var0, dir='-').doit()
    return left_limit

def calc_right_limit(f, var, var0):
    right_limit = Limit(f, var, var0, dir='+').doit()
    return right_limit

if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable to differentiate with respect to: ')
    var0 = float(input('Enter the the pint to check the continuity at: '))

    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function was entered')
    else:
        var = Symbol(var)
        left_limit = calc_left_limit(f, var, var0)
        right_limit = calc_right_limit(f, var, var0)
        f_var0 = f.subs({var:var0})
        if left_limit == right_limit == f_var0:
            print('{0} is continus at {1}'.format(f, var0))
        else:
            print('{0} is NOT continus at {1}'.format(f, var0))
