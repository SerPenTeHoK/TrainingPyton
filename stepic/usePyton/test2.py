

objects = [1, 2, 5, 'true', 1, 2, 3, 'true']

ans = 0
for obj in objects: # доступная переменная objects
    if (objects.count(obj) > 1):
        ans += 1
print(ans)