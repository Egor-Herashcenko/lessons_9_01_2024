print("hello World")
i = input([1, 2, 0, 3, 0, 4])

for a in input().split():

   i.append(int(a))

i.sort(key=lambda x: x==0)

print(i)
