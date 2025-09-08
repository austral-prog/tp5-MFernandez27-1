import math
def roots(a, b, c):
    roots = "( )"
    d = b**2 - 4*a*c#

    if d > 0:
        f1 = (-b + math.sqrt(d)) / (2*a)
        f2 = (-b - math.sqrt(d)) / (2*a)
        roots = f"({f1}, {f2})"
        return roots
    elif d == 0:
        f1 = -b / (2*a)
        roots = f"({f1})"
        return roots
    else:
        return "( )"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif b != 0 and a == 0 and c == 0:
        return f"f(x) = {b} * X"
    elif c != 0 and a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a != 0 and b != 0 and c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return "f(x) = 0"

def derivation(a, b, c):
    a = 2 * a 
    if a != 0 and b != 0:
        return f"f'(x) = {a} * X + {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {a} * X"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    else:
        return "f'(x) = 0"
