s = [int(el) for el in list(input())]
print('Счастливый') if (sum(s[0:3]) == sum(s[3:6])) else print('Обычный')
