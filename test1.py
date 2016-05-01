
objects = [1, 2, 1, 2, 3]

ans = 0
test_lst = []
for obj in objects: # доступная переменная objects
    for i in objects:
        if obj != i:
            test_lst.append(i)

    if obj not in test_lst:
        ans += 1
    test_lst.clear()

print(ans)