x = int(input())
y = input().split(" ")
lst = []

for i in y:
    i = int(i)
    lst.append(i)

sumN = x * (x + 1) / 2
sumN2 = 0
for elements in lst:
    sumN2 += elements

print(int(sumN - sumN2))
