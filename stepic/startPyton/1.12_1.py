import math

def func_p(a, b, c):
    return (a + b + c) / 2

a = int(input())
b = int(input())
c = int(input())
"""
a = 3
b = 4
c = 5
"""

p = func_p(a, b, c)
S = p * (p - a) * (p - b) * (p - c)
S = math.sqrt(S)
print(S)
