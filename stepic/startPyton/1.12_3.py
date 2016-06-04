a = float(input())
b = float(input())
op = input()

if (op == '/' or op == 'div' or op == 'mod') and b == 0 :
    print("Деление на 0!")
    exit()

if op == '+':
    print(a+b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == 'mod':
    print(a % b)
elif op == 'pow':
    print(a ** b)
elif op == 'div':
    print(a // b)

