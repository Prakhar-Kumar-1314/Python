lst = input("Enter a string: ")
lst = lst.lower()
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
lst2 = []

for char in lst:
    if char in letters:
        lst2.append(char)

x = input("Enter the element you want to count: ")

print(lst2.count(x))
