import math

def func_p(a, b, c):
    return (a + b + c) / 2

op = input()
if op == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = func_p(a, b, c)
    S = p * (p - a) * (p - b) * (p - c)
    S = math.sqrt(S)
    print(S)
elif op == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a*b)

elif op == 'круг':
    r = float(input())
    pi = 3.14
    print(pi*(r**2))
