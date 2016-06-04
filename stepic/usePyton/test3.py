
objects = [1, 2, 5, 1, 2, 2, 1, 3, True ]

ans = 0
lst = []
for obj1 in objects:
    if obj1 not in lst:
       lst.append(obj1)
       ans +=1
print(ans)