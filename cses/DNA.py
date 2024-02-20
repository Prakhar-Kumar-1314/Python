x = input("").upper()
x = list(x)
y = []
count = 0
for elements in x:
    y.append(x.count(elements))

y = set(y)
print(max(y))
