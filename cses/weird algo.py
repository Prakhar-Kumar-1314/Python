x = int(input())

print(int(x), end=" ")

while True:
    if x % 2 == 0:
        x = x/2
        print(int(x), end=" ")
    elif x == 1:
        break
    else:
        x = (x * 3) + 1
        print(int(x), end=" ")
